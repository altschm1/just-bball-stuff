from django.shortcuts import render
from .tables import MatchupTable, StatTable
from .filters import MatchupFilter, StatFilter
from .models import Matchup, PlayerStat
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

# Create your views here.
class BasicMatchupView(SingleTableMixin, FilterView):
    model = Matchup
    table_class = MatchupTable
    template_name = 'matchups/matchup.html'
    filterset_class = MatchupFilter
    extra_context={'title_head': "Matchups: Basic"}

class MatchupStatView(SingleTableMixin, FilterView):
    model = PlayerStat
    table_class = StatTable
    template_name = 'matchups/stats.html'
    filterset_class = StatFilter
    extra_context={'title_head': "Matchups: Stats"}


def glossary(request):
    return render(request, 'matchups/glossary.html')
