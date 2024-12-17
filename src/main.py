from underLogs import get_logger


logger = get_logger("my_json_logger")


class UserDomainError(Exception):
    pass

def create_user():
    try:
        raise UserDomainError("oops")
    except UserDomainError as e:
        logger.exception(e, exc_info=True)


create_user()
