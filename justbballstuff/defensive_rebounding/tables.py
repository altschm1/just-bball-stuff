import django_tables2 as tables
from .models import ReboundingStat
from django.db.models import F, FloatField
from django.db.models.functions import Cast

class TotalReboundingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    dreb = tables.Column(verbose_name="DREB", accessor="dreb")
    dboxout = tables.Column(verbose_name="DEF BOX OUT", accessor="dboxout")
    dreb_rank = tables.Column(verbose_name="DREB RANK", accessor="dreb_rank")
    dboxout_rank = tables.Column(verbose_name="DEF BOX OUT RANK", accessor="dboxout_rank")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_dreb(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dreb_rank(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout_rank(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    class Meta:
        model = ReboundingStat
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            'team',
            "age",
            "height_in",
            "weight_lb",
            "season",
            "games_played",
            "minutes_played",
            "dreb",
            "dboxout",
            "dreb_rank",
            "dboxout_rank"
        )

class PerGameReboundingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    dreb_per_game = tables.Column(verbose_name="DREB", accessor="dreb_per_game")
    dboxout_per_game = tables.Column(verbose_name="DEF BOX OUT", accessor="dboxout_per_game")
    dreb_rank_per_game = tables.Column(verbose_name="DREB RANK", accessor="dreb_rank_per_game")
    dboxout_rank_per_game = tables.Column(verbose_name="DEF BOX OUT RANK", accessor="dboxout_rank_per_game")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_dreb_per_game(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout_per_game(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dreb_rank_per_game(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout_rank_per_game(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    class Meta:
        model = ReboundingStat
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            'team',
            "age",
            "height_in",
            "weight_lb",
            "season",
            "games_played",
            "minutes_played",
            "dreb_per_game",
            "dboxout_per_game",
            "dreb_rank_per_game",
            "dboxout_rank_per_game"
        )

class PerMinReboundingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    dreb_per_min = tables.Column(verbose_name="DREB", accessor="dreb_per_min")
    dboxout_per_min = tables.Column(verbose_name="DEF BOX OUT", accessor="dboxout_per_min")
    dreb_rank_per_min = tables.Column(verbose_name="DREB RANK", accessor="dreb_rank_per_min")
    dboxout_rank_per_min = tables.Column(verbose_name="DEF BOX OUT RANK", accessor="dboxout_rank_per_min")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_dreb_per_min(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout_per_min(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dreb_rank_per_min(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_dboxout_rank_per_min(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    class Meta:
        model = ReboundingStat
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            'team',
            "age",
            "height_in",
            "weight_lb",
            "season",
            "games_played",
            "minutes_played",
            "dreb_per_min",
            "dboxout_per_min",
            "dreb_rank_per_min",
            "dboxout_rank_per_min"
        )
