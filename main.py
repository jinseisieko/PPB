import log_functions
from data import db_session


def main():
    print("Hello World")


if __name__ == '__main__':
    db_session.global_init("db/PPB.db")
    log_functions.log_information("Start")
    main()
