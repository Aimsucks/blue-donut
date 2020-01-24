from django.conf import settings
if not settings.DEBUG:
    default_app_config = 'eve_auth.apps.EveAuthConfig'
