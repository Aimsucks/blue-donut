from django.apps import AppConfig
from route_planner.backend import RoutePlannerBackend


class RoutePlannerConfig(AppConfig):
    name = 'route_planner'

    def ready(self):
        RoutePlannerBackend().updateGraph()
        pass
