import logging

from .loggers_init import config


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name=name)

__all__ = ("get_logger",)