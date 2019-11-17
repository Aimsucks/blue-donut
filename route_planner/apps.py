from django.apps import AppConfig


import logging
logger = logging.getLogger(__name__)


class RoutePlannerConfig(AppConfig):
    name = 'route_planner'

    def ready(self):
        from .backend import RoutePlannerBackend
        RoutePlannerBackend().updateGraph()
        logger.debug("Running initial graph update!")
