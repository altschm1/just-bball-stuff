import django_tables2 as tables
from django.apps import apps
from django_tables2.utils import A

PlayerProfile = apps.get_model('matchups', 'Player')

class DefensiveProfileTable(tables.Table):
    player = tables.Column(linkify=('player_profile:defensive_profile', {'player_id': tables.A('player_id'), 'season': tables.A('season')}), verbose_name="PLAYER", accessor="player")
    team = tables.Column(verbose_name="TEAM", accessor="team")
    season = tables.Column(verbose_name="SEASON", accessor="season")
    age = tables.Column(verbose_name="AGE", accessor="age")
    height_in = tables.Column(verbose_name="HEIGHT", accessor=A('get_height'), order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor="weight_lb")

    class Meta:
        model = PlayerProfile
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            "team",
            "season",
            "age",
            "height_in",
            "weight_lb"
        )

class OffensiveProfileTable(tables.Table):
    player = tables.Column(linkify=('player_profile:offensive_profile', {'player_id': tables.A('player_id'), 'season': tables.A('season')}), verbose_name="PLAYER", accessor="player")
    team = tables.Column(verbose_name="TEAM", accessor="team")
    season = tables.Column(verbose_name="SEASON", accessor="season")
    age = tables.Column(verbose_name="AGE", accessor="age")
    height_in = tables.Column(verbose_name="HEIGHT", accessor=A('get_height'), order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor="weight_lb")

    class Meta:
        model = PlayerProfile
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            "team",
            "season",
            "age",
            "height_in",
            "weight_lb"
        )
