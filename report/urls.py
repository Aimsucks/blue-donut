from django.urls import path
import report.views


app_name = 'report'


urlpatterns = [
    path('', report.views.ReportView.as_view(), name='report'),
]
