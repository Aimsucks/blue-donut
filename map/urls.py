from django.urls import path
from . import views

urlpatterns = [
    path('region/', views.RegionList.as_view()),
    path('system/', views.SystemList.as_view()),
]
