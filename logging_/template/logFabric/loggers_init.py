from .configuration import add_formatter, add_handler, add_logger, setup_config, Levels, \
    DefaultFormatters, HandlerClasses, logger_config

config = logger_config
# for example
def exception_logger() -> None:
    global config
    formatter = add_formatter(
        name="exception_formatter",
        format_string=DefaultFormatters.TimeLevelNameModuleFunctionLineMessage,
    )
    handler_1 = add_handler(
        name="exceptions_handler",
        level=Levels.WARNING,
        formatter=formatter,
        class_=HandlerClasses.FileHandler,
        filename="errors_logs.log",
    )
    add_logger("exception_logger", level=Levels.WARNING, handlers=[handler_1])


#setup loggers
setup_config(exception_logger, config=config)

__all__ = ("config",)