import logging
from enum import StrEnum

class DefaultFormatters(StrEnum):
    TimeLevelNameMessage = "{asctime} [{levelname}] {name}: {message}'"
    LevelNameMessage = "{levelname} - {name} - '{message}'"
    TimeLevelNameModuleFunctionLineMessage = ("{asctime} [{levelname}] {name} - {module}:[func {funcName}]:{lineno} "
                                              "- {message}'")

class Levels(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class HandlerClasses(StrEnum):
    ConsoleHandler = "logging.StreamHandler"
    FileHandler = "logging.FileHandler"

class NewFunctionFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.funcName == "main":
            return False
        try:  # just for example
            if record.ignore is True:
                return False
        except Exception:
            pass
        return True


logger_config = {
    "version": 1,
    "formatters": {},
    "handlers": {},
    "loggers": {},
    "filters": {},
    "disable_existing_loggers": False,
    }

def add_formatter(name: str, format_string: str | DefaultFormatters) -> str:
    global logger_config
    logger_config["formatters"][name] = {
        "format": format_string if type(format_string) is str else format_string.value,
        "style": "{",
    }
    return name

def add_filter(name: str, filter_path: str) -> str:
    """
    if filter in other module: filters.py (For example):
        1. import this filter
        2. write full path (filters.NewFilter)
    """
    global logger_config
    logger_config["filters"][name] = {
        "()": filter_path,
    }
    return name

def add_handler(
        name: str,
        level: Levels,
        class_: HandlerClasses,
        formatter: str,
        filename: str | None = None,
        filters: list[str] | None = None
) -> str:
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

    if filters:
        current_handler["filters"] = filters

    return name

def add_logger(name: str, level: Levels, handlers: list[str], propagate: bool = False) -> None:
    global logger_config
    logger_config["loggers"][name] = {
        "level": level.value,
        "handlers": handlers,
        "propagate": propagate
    }



####
def configuration_logger():
    form_1 = add_formatter("form_1", DefaultFormatters.TimeLevelNameModuleFunctionLineMessage)
    hand_1 = add_handler("hand_1", Levels.DEBUG, class_=HandlerClasses.ConsoleHandler, formatter=form_1)
    add_logger("logger_1", Levels.DEBUG, handlers=[hand_1])

def exception_logger():
    form_2 = add_formatter("exc", DefaultFormatters.TimeLevelNameModuleFunctionLineMessage)
    hand_2 = add_handler("exc", Levels.WARNING,
                         class_=HandlerClasses.FileHandler, formatter=form_2, filename="logs.log")
    add_logger("exc_logger", Levels.WARNING, handlers=[hand_2])

def filter_logger():
    formatter = add_formatter("f_formatter", DefaultFormatters.TimeLevelNameModuleFunctionLineMessage)
    filter_ = add_filter(name="f_filter", filter_path=NewFunctionFilter)
    handler_ = add_handler(name="f_handler", level=Levels.DEBUG,
                           class_=HandlerClasses.ConsoleHandler, formatter=formatter, filters=[filter_])
    add_logger(name="f_logger", level=Levels.DEBUG, handlers=[handler_])

def setup_config() -> None:
    configuration_logger()
    exception_logger()
    filter_logger()


setup_config()


__all__ = ("logger_config")


#other files
if __name__ == '__main__':

    import logging.config

    logging.config.dictConfig(logger_config)

    logger = logging.getLogger("logger_1")
    def a():
        logger.warning("warn!")
    a()