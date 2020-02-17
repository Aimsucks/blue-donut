from django.urls import path
import report.views as views

app_name = 'report'

urlpatterns = [
    path('api/report/', views.Report.as_view(), name='report'),
]
