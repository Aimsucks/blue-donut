from django.urls import path
from . import views

urlpatterns = [
    path('map/region/', views.RegionList.as_view()),
    path('map/system/', views.SystemList.as_view()),
]
