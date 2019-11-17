from django.apps import AppConfig

import logging
logger = logging.getLogger(__name__)


class RoutePlannerConfig(AppConfig):
    name = 'route_planner'

    def ready(self):
        from .backend import RoutePlannerBackend

        logger.debug("Running initial graph update.")
        RoutePlannerBackend().updateGraph()
        logger.debug("Graph update complete!")
