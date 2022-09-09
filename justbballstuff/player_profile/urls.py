from django.urls import path
from . import views

app_name = 'player_profile'

urlpatterns = [
    path('defense', views.DefenseProfileView.as_view(), name='defense_index'),
    path('defense/<str:player_id>/<str:season>/', views.defense_profile, name='defensive_profile',),
    path('offense', views.OffenseProfileView.as_view(), name='offense_index'),
    path('offense/<str:player_id>/<str:season>/', views.offense_profile, name='offensive_profile',)
]
