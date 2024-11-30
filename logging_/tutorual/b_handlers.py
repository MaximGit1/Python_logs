import logging

base_logger = logging.getLogger("base_logger")
print(base_logger.handlers)

child_logger = logging.getLogger("base_logger.child")
print(child_logger.handlers)


logging.basicConfig()  # root handler
# print(base_logger.parent.handlers)

console_child_handler = logging.StreamHandler()
child_logger.addHandler(hdlr=console_child_handler)
print(child_logger.handlers)

log_format = logging.Formatter(fmt="%(levelname)s - %(name)s - %(message)s")
console_child_handler.setFormatter(fmt=log_format)
child_logger.propagate = False

# if uncomment basicConfig & comment child_logger.propagate -->  u have 2 messages
child_logger.warning("wow!")
