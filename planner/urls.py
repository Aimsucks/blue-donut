from django.urls import path

# from rest_framework import routers
# from .api import FavoriteViewSet, RecentsViewSet

import planner.views as views

app_name = 'planner'

# router = routers.SimpleRouter()
# router.register('api/characters', CharacterViewSet, 'characters')
# router.register('api/status', LoginViewSet, 'status')

urlpatterns = [
    path('api/route/', views.GenerateRoute.as_view(), name='route'),
    path('api/popular/', views.Popular.as_view(), name='popular'),
    path('api/favorites/', views.Favorites.as_view(), name='favorites'),
    path('api/recents/', views.Recents.as_view(), name='recents'),
]

# urlpatterns += router.urls
