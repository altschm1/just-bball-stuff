from django.shortcuts import render
from .tables import TotalRimProtectionTable, PerGameRimProtectionTable, PerMinRimProtectionTable
from .filters import RimProtectionFilter
from .models import RimProtectionStat
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

# Create your views here.
class TotalRimProtectionView(SingleTableMixin, FilterView):
    model = RimProtectionStat
    table_class = TotalRimProtectionTable
    template_name = 'rim_protection/table.html'
    filterset_class = RimProtectionFilter
    extra_context={'title_head': "Rim Protection: Total", "rim_protection": True, "total": True}

class PerGameRimProtectionView(SingleTableMixin, FilterView):
    model = RimProtectionStat
    table_class = PerGameRimProtectionTable
    template_name = 'rim_protection/table.html'
    filterset_class = RimProtectionFilter
    extra_context={'title_head': "Rim Protection: Per Game", "rim_protection": True, "per_game": True}

class PerMinRimProtectionView(SingleTableMixin, FilterView):
    model = RimProtectionStat
    table_class = PerMinRimProtectionTable
    template_name = 'rim_protection/table.html'
    filterset_class = RimProtectionFilter
    extra_context={'title_head': "Rim Protection: Per 36 Mins", "rim_protection": True, "per_min": True}

def glossary(request):
    return render(request, 'rim_protection/glossary.html', {'title_head': "Rim Protection: Glossary", "rim_protection": True, "glossary": True})
