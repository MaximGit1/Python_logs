import requests
import logging

logging.basicConfig(level="DEBUG")  # set handler's level
logging.getLogger("urllib3").setLevel("ERROR")  # requests depend
logger = logging.getLogger()  # created a logger without name == root logger
logger.setLevel("DEBUG") # set DEBUG level

def main(name: str):
    logger.debug(f"App {name} is Called")
    requests.get(url="https://www.google.com")


if __name__ == '__main__':
    main("My_app")
    print(logger.parent)  # None - because has not name == root

    single_logger = logging.getLogger(name="single_logger")
    print(single_logger.parent)  # <RootLogger root (DEBUG)> - because singleton
