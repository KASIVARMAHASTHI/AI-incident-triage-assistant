import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("incident-triage")


def log(message: str):
    logger.info(message)
