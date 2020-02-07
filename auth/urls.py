from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework import routers
from .api import CharacterViewSet

import auth.views as auth

app_name = 'auth'

router = routers.SimpleRouter()
router.register('api/characters', CharacterViewSet, 'characters')

urlpatterns = [
    path('auth/login/', auth.Login.as_view(), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/callback', auth.Callback.as_view(), name='callback'),
]

urlpatterns += router.urls
