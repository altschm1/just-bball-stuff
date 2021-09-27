from django.urls import path
from . import views

app_name = 'player_profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='defense_index'),
    path('<str:player_id>/<str:season>/', views.defense_profile, name='defensive_profile',),
]
