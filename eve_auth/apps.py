from django.apps import AppConfig

from eve_esi import EsiManager


class EveAuthConfig(AppConfig):
    name = 'eve_auth'

    def ready(self):
        EsiManager()._initialize_app()
