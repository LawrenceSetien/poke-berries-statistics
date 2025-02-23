import logging as logger


def setup_logger(name, level=logger.INFO):
    """Function to setup a logger"""
    formatter = logger.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Stream handler
    stream_handler = logger.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger_handler = logger.getLogger(name)
    logger_handler.setLevel(level)
    logger_handler.addHandler(stream_handler)

    return logger_handler

logging = setup_logger('poke_logger', logger.INFO)