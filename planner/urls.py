from django.urls import path
import planner.views as views

app_name = 'planner'

urlpatterns = [
    path('api/route/', views.GenerateRoute.as_view(), name='route'),
    path('api/route/confirm/', views.SendRoute.as_view(), name='send'),
    path('api/popular/', views.Popular.as_view(), name='popular'),
    path('api/favorites/', views.Favorites.as_view(), name='favorites'),
    path('api/recents/', views.Recents.as_view(), name='recents'),
]
