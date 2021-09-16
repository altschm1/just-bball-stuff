from django.shortcuts import render
from .tables import TotalDefensivePlaymakingTable, PerGameDefensivePlaymakingTable, PerMinDefensivePlaymakingTable, RankPerGameDefensivePlaymakingTable, RankPerMinDefensivePlaymakingTable
from .filters import DefensivePlaymakingFilter
from .models import DefensivePlaymakingStat
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

# Create your views here.
class TotalDefensivePlaymakingView(SingleTableMixin, FilterView):
    model = DefensivePlaymakingStat
    table_class = TotalDefensivePlaymakingTable
    template_name = 'defensive_playmaking/table.html'
    filterset_class = DefensivePlaymakingFilter
    extra_context={'title_head': "Defensive Playmaking: Total", "defensive_playmaking": True, "total": True}

class PerGameDefensivePlaymakingView(SingleTableMixin, FilterView):
    model = DefensivePlaymakingStat
    table_class = PerGameDefensivePlaymakingTable
    template_name = 'defensive_playmaking/table.html'
    filterset_class = DefensivePlaymakingFilter
    extra_context={'title_head': "Defensive Playmaking: Per Game", "defensive_playmaking": True, "per_game": True}

class PerMinDefensivePlaymakingView(SingleTableMixin, FilterView):
    model = DefensivePlaymakingStat
    table_class = PerMinDefensivePlaymakingTable
    template_name = 'defensive_playmaking/table.html'
    filterset_class = DefensivePlaymakingFilter
    extra_context={'title_head': "Defensive Playmaking: Per 36 Mins", "defensive_playmaking": True, "per_min": True}

class RankPerGameDefensivePlaymakingView(SingleTableMixin, FilterView):
    model = DefensivePlaymakingStat
    table_class = RankPerGameDefensivePlaymakingTable
    template_name = 'defensive_playmaking/table.html'
    filterset_class = DefensivePlaymakingFilter
    extra_context={'title_head': "Defensive Playmaking: Rank Per Game", "defensive_playmaking": True, "per_game_rank": True}

class RankPerMinDefensivePlaymakingView(SingleTableMixin, FilterView):
    model = DefensivePlaymakingStat
    table_class = RankPerMinDefensivePlaymakingTable
    template_name = 'defensive_playmaking/table.html'
    filterset_class = DefensivePlaymakingFilter
    extra_context={'title_head': "Defensive Playmaking: Rank Per Min", "defensive_playmaking": True, "per_min_rank": True}

def glossary(request):
    return render(request, 'defensive_playmaking/glossary.html', {'title_head': "Defensive Playmaking: Glossary", "defensive_playmaking": True, "glossary": True})
