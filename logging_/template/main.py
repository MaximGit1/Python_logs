from logFabric import get_logger

logger = get_logger(name="exception_logger")

def main(res):
    try:
        return res.count()
    except AttributeError:
        logger.exception(f"error!")
        return -1
    except Exception as e:
        logger.critical(f"{e}")
        return -1


if __name__ == '__main__':
    print(main(12))