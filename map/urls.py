from django.urls import path

import map.views as views

app_name = 'map'

urlpatterns = [
    path('api/systems/', views.SystemsView.as_view(), name='systems'),
]
