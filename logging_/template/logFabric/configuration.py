import logging.config

from typing import Callable
from enum import StrEnum


class DefaultFormatters(StrEnum):
    TimeLevelNameMessage = "{asctime} [{levelname}] {name}: {message}'"
    LevelNameMessage = "{levelname} - {name} - '{message}'"
    TimeLevelNameModuleFunctionLineMessage = ("{asctime} [{levelname}] {name} - "
                                              "{module}:[func {funcName}]:{lineno} - {message}'")


class Levels(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class HandlerClasses(StrEnum):
    ConsoleHandler = "logging.StreamHandler"
    FileHandler = "logging.FileHandler"


logger_config = {
    "version": 1,
    "formatters": {},
    "handlers": {},
    "loggers": {},
    "disable_existing_loggers": False,
}


def add_formatter(name: str, format_string: str | DefaultFormatters) -> str:
    global logger_config
    logger_config["formatters"][name] = {
        "format": format_string if type(format_string) is str else format_string.value,
        "style": "{",
    }
    return name


def add_handler(name: str, level: Levels, class_: HandlerClasses, formatter: str, filename: str | None = None) -> str:
    global logger_config
    current_handler = logger_config["handlers"][name] = {
        "level": level.value,
        "class": class_.value,
        "formatter": formatter,
    }
    if class_ is HandlerClasses.FileHandler:
        if filename is None:
            raise TypeError(f"{filename} - Invalid path")
        current_handler["filename"] = filename
    return name


def add_logger(name: str, level: Levels, handlers: list[str], propagate: bool = False) -> None:
    global logger_config
    logger_config["loggers"][name] = {
        "level": level.value,
        "handlers": handlers,
        "propagate": propagate
    }


def setup_config(*args: list[Callable], config: dict) -> None:
    for logger in args:
        logger()
    logging.config.dictConfig(config)


__all__ = ("add_formatter", "add_handler", "add_logger", "logger_config", "setup_config",
           "DefaultFormatters", "Levels", "HandlerClasses")
