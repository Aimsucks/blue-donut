from django.apps import AppConfig


class PlannerConfig(AppConfig):
    name = 'planner'

    def ready(self):
        from .backend import GraphGenerator
        GraphGenerator().update_graph()
