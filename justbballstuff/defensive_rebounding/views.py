from django.shortcuts import render
from .tables import TotalReboundingTable, PerGameReboundingTable, PerMinReboundingTable
from .filters import ReboundingFilter
from .models import ReboundingStat
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

# Create your views here.
class TotalReboundingView(SingleTableMixin, FilterView):
    model = ReboundingStat
    table_class = TotalReboundingTable
    template_name = 'defensive_rebounding/table.html'
    filterset_class = ReboundingFilter
    extra_context={'title_head': "Defensive Rebounding: Total", "defensive_rebounding": True, "total": True}

class PerGameReboundingView(SingleTableMixin, FilterView):
    model = ReboundingStat
    table_class = PerGameReboundingTable
    template_name = 'defensive_rebounding/table.html'
    filterset_class = ReboundingFilter
    extra_context={'title_head': "Defensive Rebounding: Per Game", "defensive_rebounding": True, "per_game": True}

class PerMinReboundingView(SingleTableMixin, FilterView):
    model = ReboundingStat
    table_class = PerMinReboundingTable
    template_name = 'defensive_rebounding/table.html'
    filterset_class = ReboundingFilter
    extra_context={'title_head': "Defensive Rebounding: Per 36 Mins", "defensive_rebounding": True, "per_min": True}

def glossary(request):
    return render(request, 'defensive_rebounding/glossary.html', {'title_head': "Defensive Rebounding: Glossary", "defensive_rebounding": True, "glossary": True})
