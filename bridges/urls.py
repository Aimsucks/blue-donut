from django.urls import path

import bridges.views as views

app_name = 'bridges'

urlpatterns = [
    path('api/bridges/auto/', views.AutoUpdateBridges.as_view(), name='auto_update_bridges'),
    path('api/bridges/manual/', views.ManualUpdateBridges.as_view(), name='manual_update_bridges'),
]
