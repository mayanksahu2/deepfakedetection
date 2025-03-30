import sys
from src.pipelines.exception import CustomException
from src.pipelines.logger import logging


if __name__ == "__main__":
    logging.info("the execution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
