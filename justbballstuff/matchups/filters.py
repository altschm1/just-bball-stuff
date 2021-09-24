# update
import django_filters
from .models import Matchup, Player, PlayerStat

players = Player.objects.all()

def get_teams():
    teams = players.values('team').distinct().order_by('team')
    return [(t['team'], t['team']) for t in teams]

def get_seasons():
    seasons = players.values('season').distinct().order_by('season')
    return [(s['season'], s['season']) for s in seasons]


class MatchupFilter(django_filters.FilterSet):
    offense_player__player = django_filters.CharFilter(label="Player", lookup_expr='icontains')
    offense_player__team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    offense_player__age = django_filters.RangeFilter(label="Player Age Range")
    offense_player__height_in = django_filters.RangeFilter(label="Player Height (in inches) Range")
    offense_player__weight_lb = django_filters.RangeFilter(label="Player Weight (in pounds) Range")
    defense_player__player = django_filters.CharFilter(label="Player", lookup_expr='icontains')
    defense_player__team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    defense_player__age = django_filters.RangeFilter(label="Player Age Range")
    defense_player__height_in = django_filters.RangeFilter(label="Player Height (in inches) Range")
    defense_player__weight_lb = django_filters.RangeFilter(label="Player Weight (in pounds) Range")
    season = django_filters.MultipleChoiceFilter(label="Season", choices = get_seasons())
    seconds = django_filters.NumberFilter(field_name='seconds', label='Minimum Seconds', lookup_expr='gte')
    possessions = django_filters.NumberFilter(field_name='possessions', label='Minimum Possessions', lookup_expr='gte')

    class Meta:
        model = Matchup
        fields = (
            'offense_player__player',
            'offense_player__team',
            'offense_player__age',
            'offense_player__height_in',
            'offense_player__weight_lb',
            'defense_player__player',
            'defense_player__team',
            'defense_player__age',
            'defense_player__height_in',
            'defense_player__weight_lb',
            'season',
            'seconds',
            'possessions',
        )

class StatFilter(django_filters.FilterSet):
    player__player = django_filters.CharFilter(label="Player", lookup_expr='icontains')
    player__team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    player__age = django_filters.RangeFilter(label="Player Age Range")
    player__height_in = django_filters.RangeFilter(label="Player Height (in inches) Range")
    player__weight_lb = django_filters.RangeFilter(label="Player Weight (in pounds) Range")
    season = django_filters.MultipleChoiceFilter(label="Season", choices = get_seasons())
    poss = django_filters.NumberFilter(field_name='poss', label='Minimum Possessions', lookup_expr='gte')
    usage_score = django_filters.RangeFilter(label="Usage Score Range")
    versatility_score = django_filters.RangeFilter(label="Versatility Score Range")
    matchup_height = django_filters.RangeFilter(label="Opposing Matchup Height (in inches) Range")
    matchup_weight = django_filters.RangeFilter(label="Opposing Matchup Weight (in pounds) Range")
    poss_vs_lte75 = django_filters.NumberFilter(field_name='poss_vs_lte75', label="Minimum Possessions versus <= 6'3", lookup_expr='gte')
    poss_vs_lte78 = django_filters.NumberFilter(field_name='poss_vs_lte78', label="Minimum Possessions versus 6'4 to 6'6", lookup_expr='gte')
    poss_vs_lte81 = django_filters.NumberFilter(field_name='poss_vs_lte81', label="Minimum Possessions versus 6'7 to 6'9", lookup_expr='gte')
    poss_vs_gte82 = django_filters.NumberFilter(field_name='poss_vs_gte82', label="Minimum Possessions versus >= 6'10", lookup_expr='gte')

    class Meta:
        model = PlayerStat
        fields = (
            'player__player',
            'player__team',
            'player__age',
            'player__height_in',
            'player__weight_lb',
            'season',
            'poss',
        )
