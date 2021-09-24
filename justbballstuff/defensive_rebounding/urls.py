from django.urls import path
from . import views

app_name = 'defensive_rebounding'

urlpatterns = [
    path('total/', views.TotalReboundingView.as_view(), name='total'),
    path('per-game/', views.PerGameReboundingView.as_view(), name='per_game'),
    path('per-36/', views.PerMinReboundingView.as_view(), name='per_min'),
    path('glossary/', views.glossary, name='glossary'),
]
