from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    re_path('', include('frontend.urls')),
]
