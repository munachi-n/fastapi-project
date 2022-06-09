import logging
from typing import Any

logger = logging.getLogger(__name__)


def log_info(message: str):
    logger.info(message)


def log_error(message: str, error: Exception = None):
    if error:
        logger.error(f"{message}: {str(error)}")
    else:
        logger.error(message)


def log_warning(message: str):
    logger.warning(message)


def log_debug(message: str):
    logger.debug(message)
