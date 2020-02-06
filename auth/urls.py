from django.urls import path
from django.contrib.auth import views as auth_views

import auth.views as auth

app_name = 'auth'

urlpatterns = [
    path('login/', auth.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('callback', auth.Callback.as_view(), name='callback'),
    path('check/', auth.Check.as_view(), name='check')
]
