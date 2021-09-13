from django.urls import path
from . import views

app_name = 'matchups'

urlpatterns = [
    path('basic/', views.BasicMatchupView.as_view(), name='basic'),
    path('matchup-stats/', views.MatchupStatView.as_view(), name='stats'),
    path('glossary/', views.glossary, name='glossary')
]
