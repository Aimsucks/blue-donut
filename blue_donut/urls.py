from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('planner/', include('route_planner.urls')),
    path('report/', include('report.urls')),
    path('auth/', include('eve_auth.urls', namespace='eve_auth')),
    path('manager/', include('jump_bridges.urls')),
    path('admin/', admin.site.urls),
]
