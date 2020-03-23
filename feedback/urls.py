from django.urls import path
import feedback.views as views

app_name = 'feedback'

urlpatterns = [
    path('api/feedback/', views.Feedback.as_view(), name='feedback'),
]
