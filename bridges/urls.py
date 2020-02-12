from django.urls import path

import bridges.views as views

app_name = 'bridges'

urlpatterns = [
    path('api/bridges/update/', views.UpdateBridges.as_view(), name='update_bridges'),
]
