from django.urls import path
from . import views

app_name = 'defensive_playmaking'

urlpatterns = [
    path('total/', views.TotalDefensivePlaymakingView.as_view(), name='total'),
    path('per-game/', views.PerGameDefensivePlaymakingView.as_view(), name='per_game'),
    path('per-36/', views.PerMinDefensivePlaymakingView.as_view(), name='per_min'),
    path('rank-per-game/', views.RankPerGameDefensivePlaymakingView.as_view(), name='rank_per_game'),
    path('rank-per-min/', views.RankPerMinDefensivePlaymakingView.as_view(), name='rank_per_min'),
    path('glossary/', views.glossary, name='glossary'),
]
