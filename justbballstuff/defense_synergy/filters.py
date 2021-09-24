from .models import DefensiveSynergyStat
import django_filters

stats = DefensiveSynergyStat.objects.all()

def get_teams():
    teams = stats.values('team').distinct().order_by('team')
    return [(t['team'], t['team']) for t in teams]

def get_seasons():
    seasons = stats.values('season').distinct().order_by('season')
    return [(s['season'], s['season']) for s in seasons]

class DefensiveSynergyFilter(django_filters.FilterSet):
    player = django_filters.CharFilter(label="Player", lookup_expr='icontains')
    team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    age = django_filters.RangeFilter(label="Player Age Range")
    height_in = django_filters.RangeFilter(label="Player Height (in inches) Range")
    weight_lb = django_filters.RangeFilter(label="Player Weight (in pounds) Range")
    season = django_filters.MultipleChoiceFilter(label="Season", choices = get_seasons())
    games_played = django_filters.NumberFilter(field_name='games_played', label='Minimum Games Played', lookup_expr='gte')
    minutes_played = django_filters.NumberFilter(field_name='minutes_played', label='Minimum Minutes Played', lookup_expr='gte')

    class Meta:
        model = DefensiveSynergyStat
        fields = (
            "player",
            'team',
            "age",
            "height_in",
            "weight_lb",
            "season",
            "games_played",
            "minutes_played",
        )
