import sys
import logging
from logging import config
from multiprocessing import Queue
from multiprocessing.context import Process
from typing import List

import environ

from event.organisation_event_processor import OrganisationEventProcessor
from event.utils.config import KafkaConfig
from event.utils.ils_event_consumer import IlsEventConsumer
from utils.token import IlsApiTokenRefresher

env = environ.FileAwareEnv()
env.read_env(env.str('/home/akira/Documents/DS/Benny-code/Python-Unterlagen/ptw-service/', 'local.env'))

# get time
import datetime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%H:%M:%S')
# Save logs to logs folder
import os
if not os.path.exists('logs'):
   os.makedirs('logs')
#fileHandler = f"logs/{formatted_time}.log"
fileHandler = "teste-agrcagou.log"

log_level = env('LOG_LEVEL', default="DEBUG")

log_config = {
    "version": 1,
    "root": {
        "handlers": ["console","file"],
        "level": log_level
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": log_level,
            "stream": sys.stdout
        }
        ,
        "file":{
            "class":"logging.handlers.RotatingFileHandler",
            #"mode":"a",
            #"level": log_level,
            "formatter":"std_out",
            "filename":fileHandler,
            "maxBytes":1048576,
            "backupCount":3,
        }
    },
    "formatters": {
        "std_out": {
            "format": '[%(asctime)s] "%(levelname)s" "%(module)s" "%(message)s"',
            "datefmt": "%d/%b/%Y %I:%M:%S"
        }   
    },
}

config.dictConfig(log_config)
#config.fileConfig(fname)

logger = logging.getLogger(__name__)
#rootLogger = logging.getLogger()
#rootLogger.addHandler(fileHandler)

def start_application():
    logger.info("Starting application...")

    processes: List[Process] = []
    message_queue = Queue()

    consumer = IlsEventConsumer(message_queue)

    kafka_config = KafkaConfig()

    token_refresher = IlsApiTokenRefresher()

    logger.info(f'ils-api access: {token_refresher.get_token().is_valid()}')

    processes.append(
        OrganisationEventProcessor(message_queue, kafka_config=kafka_config, token_refresher=token_refresher))

    for process in processes:
        logger.debug(f"Starting process: '{process.name}'")
        process.start()

    consumer.start_consumer()

    for process in processes:
        logger.debug(f"Ending process: '{process.name}'")
        process.join()
        process.close()
        logger.info(f"Process {process.name} as fully stopped!")


if __name__ == '__main__':
    start_application()
