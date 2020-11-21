import colorlog


def setup_logger():
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M'))

    logger = colorlog.getLogger(__name__)
    logger.addHandler(handler)
    return logger
