from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth'
    verbose_name = 'EVE SSO'
    label = 'eve_auth'

    def ready(self):
        from django.conf import settings
        if not settings.DEBUG:
            from esi import ESIManager

            # logger.debug("Running startup ESI initialization.")
            ESIManager()._initialize_app()
            # logger.debug("ESI initialization complete!")
