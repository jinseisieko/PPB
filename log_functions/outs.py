import datetime


def __add_time_decorator(func):
    def wrapper(text: str):
        time = datetime.datetime.now()
        text = f"[{time}]\t" + text
        return func(text)

    return wrapper


@__add_time_decorator
def log_exception(text: str) -> None:
    message = "[exception]\t" + text
    with open("log.txt", "a") as file:
        file.write(message + "\n")
    print("\033[31m{}".format(message) + "\033[0m")


@__add_time_decorator
def log_warning(text: str) -> None:
    message = "[warning]\t" + text
    with open("log.txt", "a") as file:
        file.write(message + "\n")
    print("\033[33m{}".format(message) + "\033[0m")


@__add_time_decorator
def log_information(text: str) -> None:
    message = "[information]\t" + text
    with open("log.txt", "a") as file:
        file.write(message + "\n")
    print("\033[32m{}".format(message) + "\033[0m")
