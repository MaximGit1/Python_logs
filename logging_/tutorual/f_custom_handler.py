from abc import abstractmethod
from typing import Protocol
import logging


class HandlerProtocol(Protocol):
    @abstractmethod
    def emit(self, record: logging.LogRecord) -> None: ...


class CustomHandler(HandlerProtocol, logging.Handler):
    def __init__(self, file_name: str):
        logging.Handler.__init__(self)
        self.file_name = file_name
        self.level = 20


    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record=record)
        # logic
        with open(self.file_name, 'a') as f:
            f.write("custom " + message + "\n")

logger = logging.getLogger("custom_logger")
logger.addHandler(hdlr=CustomHandler("custom_logs.log"))
logger.warning("omg")
