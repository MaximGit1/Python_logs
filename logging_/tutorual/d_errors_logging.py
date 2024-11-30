import logging.config

from c_configurations import logger_config

logging.config.dictConfig(config=logger_config)
logger = logging.getLogger("exc_logger")

def calculate_result(nums: list[int]):
    res = 0
    for num in nums:
        try:
            res += 1 / num
        except ZeroDivisionError as e:
            logger.exception(f"num={num}")  # like WARNING
    return


calculate_result([12, 432, 53, 0, - 4])
