import django_filters
from django.apps import apps
PlayerProfile = apps.get_model('matchups', 'Player')

players = PlayerProfile.objects.all()

def get_teams():
    teams = players.values('team').distinct().order_by('team')
    return [(t['team'], t['team']) for t in teams]

def get_seasons():
    seasons = players.values('season').distinct().order_by('season')
    return [(s['season'], s['season']) for s in seasons]

class ProfileFilter(django_filters.FilterSet):
    player = django_filters.CharFilter(label="Player", lookup_expr='icontains')
    team = django_filters.MultipleChoiceFilter(label="Team", choices=get_teams())
    season = django_filters.MultipleChoiceFilter(label="Season", choices = get_seasons())

    class Meta:
        model = PlayerProfile
        fields = (
            "player",
            'team',
            "season",
        )
