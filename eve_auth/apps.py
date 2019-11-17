from django.apps import AppConfig

import logging
logger = logging.getLogger(__name__)


class EveAuthConfig(AppConfig):
    name = 'eve_auth'

    def ready(self):
        from eve_esi import EsiManager

        logger.debug("Running startup ESI initialization.")
        EsiManager()._initialize_app()
        logger.debug("ESI initialization complete!")
