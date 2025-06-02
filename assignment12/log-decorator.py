import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(
            logging.INFO,
            f"function: {func.__name__} "
            f"positional parameters: {args if args else 'none'} "
            f"keyword parameters: {kwargs if kwargs else 'none'} "
            f"return: {result}"
        )
        return result
    return wrapper

@logger_decorator
def greet():
    print("Hello, World!")

@logger_decorator
def check_args(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    greet()   # Yes printing the Hello World
    check_args(1, 2, 3, 4)
    return_decorator(a=1, b=2, c="test")