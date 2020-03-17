from django.urls import path
import management.views as views

app_name = 'management'

urlpatterns = [
    path('api/statistics/', views.Statistics.as_view(), name='statistics'),
]
