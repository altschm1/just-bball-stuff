from django.urls import path
from . import views

app_name = 'rim_protection'

urlpatterns = [
    path('total/', views.TotalRimProtectionView.as_view(), name='total'),
    path('per-game/', views.PerGameRimProtectionView.as_view(), name='per_game'),
    path('per-36/', views.PerMinRimProtectionView.as_view(), name='per_min'),
    path('glossary/', views.glossary, name='glossary'),
]
