from django.urls import path
import jump_bridges.views


app_name = 'jump_bridges'

urlpatterns = [
    path('', jump_bridges.views.ManagerView.as_view(), name='manager'),
]
