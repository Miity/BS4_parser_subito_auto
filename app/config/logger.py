import logging
from .settings import Settings

__all__ = [
    'logger',
]

logger = logging.getLogger(Settings.LOGGER_NAME)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                              '[%(module)s - %(filename)s - %(funcName)s - %(lineno)d]:\n'
                              ' %(message)s',
                              datefmt='%Y-%m-%d-%H:%M:%S')
if Settings.LOGGING_IN_STDOUT:
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

if Settings.LOGGING_IN_FILE:
    fh = logging.FileHandler(f'{Settings.LOGGER_NAME}.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)