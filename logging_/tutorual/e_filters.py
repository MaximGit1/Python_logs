import logging.config

from c_configurations import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger("f_logger")


def a():
    logger.warning("warn!", extra={"ignore": True})

def main():
    logger.warning("main!")

def start_app():
    logger.warning("start!")

if __name__ == '__main__':
    main()
    start_app()
    a()