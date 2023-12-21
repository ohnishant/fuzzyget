import logging


def get_logger(
    LOG_NAME: str = __name__,
    LOG_FORMAT: str = "%(asctime)s %(name)-12s - %(levelname)s - %(message)s",
    LOG_FILE_INFO: str = "logs/fuzzyget.log",
    LOG_FILE_ERR: str = "logs/fuzzyget.err",
    DATE_FMT: str = "%d-%b-%y %H:%M:%S",
) -> logging.Logger:
    logger = logging.getLogger(LOG_NAME)
    logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FMT)

    # Console Output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(logging.WARN)
    logger.addHandler(stream_handler)

    file_handler_error = logging.FileHandler(filename=LOG_FILE_ERR, mode="a")
    file_handler_error.setLevel(logging.WARN)
    file_handler_error.setFormatter(log_formatter)
    logger.addHandler(file_handler_error)

    file_handler_info = logging.FileHandler(filename=LOG_FILE_INFO, mode="a")
    file_handler_info.setLevel(logging.DEBUG)
    file_handler_info.setFormatter(log_formatter)
    logger.addHandler(file_handler_info)

    return logger


def main():
    my_logger: logging.Logger = get_logger()

    my_logger.debug("debug message")
    my_logger.info("This is an info logging message")
    my_logger.warning("This is an warning message")
    my_logger.error("This is an error message")


if __name__ == "__main__":
    main()
