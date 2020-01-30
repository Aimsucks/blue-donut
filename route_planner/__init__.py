from django.conf import settings
if not settings.DEBUG:
    default_app_config = 'route_planner.apps.RoutePlannerConfig'
