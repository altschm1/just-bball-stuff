from django.urls import path
from . import views

app_name = 'defense_synergy'

urlpatterns = [
    path('total/', views.TotalDefensiveSynergyView.as_view(), name='total'),
    path('per-game/', views.PerGameDefensiveSynergyView.as_view(), name='per_game'),
    path('per-36/', views.PerMinDefensiveSynergyView.as_view(), name='per_min'),
    path('summary/', views.SummaryDefensiveSynergyView.as_view(), name='summary'),
    path('glossary/', views.glossary, name='glossary'),
]
