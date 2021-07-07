"""
created by Nagaj at 06/07/2021
"""
import sys
from app.config import LOG_FORMAT
from loguru import logger


# logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format=LOG_FORMAT,
)
