from django.apps import AppConfig


class EveAuthConfig(AppConfig):
    name = 'eve_auth'

    def ready(self):
        from eve_esi import EsiManager
        EsiManager()._initialize_app()
