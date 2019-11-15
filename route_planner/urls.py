from django.urls import path
import route_planner.views


app_name = 'route_planner'


urlpatterns = [
    path('', route_planner.views.PlannerView.as_view(), name='planner')
]
