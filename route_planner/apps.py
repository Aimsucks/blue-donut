from django.apps import AppConfig
from route_planner.backend import RoutePlannerBackend

import logging
logger = logging.getLogger(__name__)


class RoutePlannerConfig(AppConfig):
    name = 'route_planner'

    def ready(self):
        RoutePlannerBackend().updateGraph()
        logger.debug("Running initial graph update!")
