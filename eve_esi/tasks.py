import logging

from eve_esi import ESI


logger = logging.getLogger(__name__)


def initialize_esi():
    logger.info("Initializing ESI application to start Huey consumer")
    ESI._initialize_app()
    logger.info("ESI application initialized for consumer!")
