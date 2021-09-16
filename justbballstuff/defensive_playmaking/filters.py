from .models import DefensivePlaymakingStat
import django_filters

stats = DefensivePlaymakingStat.objects.all()

def get_players():
    player_names = stats.values('player').distinct().order_by('player')
    return [(p['player'], p['player']) for p in player_names]

def get_teams():
    teams = stats.values('team').distinct().order_by('team')
    return [(t['team'], t['team']) for t in teams]

def get_seasons():
    seasons = stats.values('season').distinct().order_by('season')
    return [(s['season'], s['season']) for s in seasons]


class DefensivePlaymakingFilter(django_filters.FilterSet):
    player = django_filters.ChoiceFilter(label="Player", choices=get_players())
    team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    age = django_filters.RangeFilter(label="Player Age Range")
    height_in = django_filters.RangeFilter(label="Player Height (in inches) Range")
    weight_lb = django_filters.RangeFilter(label="Player Weight (in pounds) Range")
    season = django_filters.MultipleChoiceFilter(label="Season", choices = get_seasons())
    games_played = django_filters.NumberFilter(field_name='games_played', label='Minimum Games Played', lookup_expr='gte')
    minutes_played = django_filters.NumberFilter(field_name='minutes_played', label='Minimum Minutes Played', lookup_expr='gte')
    steals = django_filters.RangeFilter(label="Steal(s) Range")
    blocks = django_filters.RangeFilter(label="Block(s) Range")
    deflections = django_filters.RangeFilter(label="Deflection(s) Range")
    deals = django_filters.RangeFilter(label="Deal(s) Range")
    stocks = django_filters.RangeFilter(label="Stock(s) Range")

    class Meta:
        model = DefensivePlaymakingStat
        fields = (
            "player",
            'team',
            "age",
            "height_in",
            "weight_lb",
            "season",
            "games_played",
            "minutes_played",
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )
