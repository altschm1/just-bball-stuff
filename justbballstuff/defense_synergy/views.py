from django.shortcuts import render
from .tables import TotalDefensiveSynergyTable, PerGameDefensiveSynergyTable, PerMinDefensiveSynergyTable, SummaryDefensiveSynergyTable
from .filters import DefensiveSynergyFilter
from .models import DefensiveSynergyStat
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

# Create your views here.
class TotalDefensiveSynergyView(SingleTableMixin, FilterView):
    model = DefensiveSynergyStat
    table_class = TotalDefensiveSynergyTable
    template_name = 'defense_synergy/table.html'
    filterset_class = DefensiveSynergyFilter
    extra_context={'title_head': "Defensive Synergy: Total", "defense_synergy": True, "total": True}

class PerGameDefensiveSynergyView(SingleTableMixin, FilterView):
    model = DefensiveSynergyStat
    table_class = PerGameDefensiveSynergyTable
    template_name = 'defense_synergy/table.html'
    filterset_class = DefensiveSynergyFilter
    extra_context={'title_head': "Defensive Synergy: Per Game", "defense_synergy": True, "per_game": True}

class PerMinDefensiveSynergyView(SingleTableMixin, FilterView):
    model = DefensiveSynergyStat
    table_class = PerMinDefensiveSynergyTable
    template_name = 'defense_synergy/table.html'
    filterset_class = DefensiveSynergyFilter
    extra_context={'title_head': "Defensive Synergy: Per 36 Mins", "defense_synergy": True, "per_min": True}

class SummaryDefensiveSynergyView(SingleTableMixin, FilterView):
    model = DefensiveSynergyStat
    table_class = SummaryDefensiveSynergyTable
    template_name = 'defense_synergy/table.html'
    filterset_class = DefensiveSynergyFilter
    extra_context={'title_head': "Defensive Synergy: Summary", "defense_synergy": True, "summary": True}

def glossary(request):
    return render(request, 'defense_synergy/glossary.html', {'title_head': "Defensive Synergy: Glossary", "defense_synergy": True, "glossary": True})
