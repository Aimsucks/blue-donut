from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth.urls')),
    path('', include('planner.urls')),
    path('', include('bridges.urls')),
    path('', include('map.urls')),
    path('', include('report.urls')),
    path('', include('frontend.urls')),
]
