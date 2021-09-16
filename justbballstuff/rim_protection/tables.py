import django_tables2 as tables
from .models import RimProtectionStat
from django.db.models import F, FloatField
from django.db.models.functions import Cast

class TotalRimProtectionTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    freq = tables.Column(verbose_name="FREQ%", accessor="freq")
    def_fgm = tables.Column(verbose_name="DFGM", accessor="def_fgm")
    def_fga = tables.Column(verbose_name="DFGA", accessor="def_fga")
    def_fg_pct = tables.Column(verbose_name="DFG%", accessor="def_fg_pct")
    points_saved = tables.Column(verbose_name="PTS SAVED", accessor="points_saved")
    def_fg_pct_score = tables.Column(verbose_name="DFG% SCORE", accessor="def_fg_pct_score")
    points_saved_score = tables.Column(verbose_name="PTS SAVED SCORE", accessor="points_saved_score")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_def_fg_pct(self, value, record):
        return f"{value:.2f}"

    def render_points_saved(self, value, record):
        return f"{value:.2f}"

    def render_def_fg_pct_score(self, value, record):
        return f"{value:.2f}"

    def render_points_saved_score(self, value, record):
        return f"{value:.2f}"

    class Meta:
        model = RimProtectionStat
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
            "freq",
            "def_fgm",
            "def_fga",
            "def_fg_pct",
            "points_saved",
            "def_fg_pct_score",
            "points_saved_score"
        )

class PerGameRimProtectionTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    freq = tables.Column(verbose_name="FREQ%", accessor="freq")
    def_fgm_per_game = tables.Column(verbose_name="DFGM", accessor="def_fgm_per_game")
    def_fga_per_game = tables.Column(verbose_name="DFGA", accessor="def_fga_per_game")
    def_fg_pct = tables.Column(verbose_name="DFG%", accessor="def_fg_pct")
    points_saved_per_game = tables.Column(verbose_name="PTS SAVED", accessor="points_saved_per_game")
    def_fg_pct_score = tables.Column(verbose_name="DFG% SCORE", accessor="def_fg_pct_score")
    points_saved_per_game_score = tables.Column(verbose_name="PTS SAVED SCORE", accessor="points_saved_per_game_score")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_def_fgm_per_game(self, value, record):
        return f"{value:.2f}"

    def render_def_fga_per_game(self, value, record):
        return f"{value:.2f}"

    def render_def_fg_pct(self, value, record):
        return f"{value:.2f}"

    def render_points_saved_per_game(self, value, record):
        return f"{value:.2f}"

    def render_def_fg_pct_score(self, value, record):
        return f"{value:.2f}"

    def render_points_saved_per_game_score(self, value, record):
        return f"{value:.2f}"

    class Meta:
        model = RimProtectionStat
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
            "freq",
            "def_fgm_per_game",
            "def_fga_per_game",
            "def_fg_pct",
            "points_saved_per_game",
            "def_fg_pct_score",
            "points_saved_per_game_score"
        )

class PerMinRimProtectionTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    freq = tables.Column(verbose_name="FREQ%", accessor="freq")
    def_fgm_per_min = tables.Column(verbose_name="DFGM", accessor="def_fgm_per_min")
    def_fga_per_min = tables.Column(verbose_name="DFGA", accessor="def_fga_per_min")
    def_fg_pct = tables.Column(verbose_name="DFG%", accessor="def_fg_pct")
    points_saved_per_min = tables.Column(verbose_name="PTS SAVED", accessor="points_saved_per_min")
    def_fg_pct_score = tables.Column(verbose_name="DFG% SCORE", accessor="def_fg_pct_score")
    points_saved_per_min_score = tables.Column(verbose_name="PTS SAVED SCORE", accessor="points_saved_per_min_score")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_def_fgm_per_min(self, value, record):
        return f"{value:.2f}"

    def render_def_fga_per_min(self, value, record):
        return f"{value:.2f}"

    def render_def_fg_pct(self, value, record):
        return f"{value:.2f}"

    def render_points_saved_per_min(self, value, record):
        return f"{value:.2f}"

    def render_def_fg_pct_score(self, value, record):
        return f"{value:.2f}"

    def render_points_saved_per_min_score(self, value, record):
        return f"{value:.2f}"


    class Meta:
        model = RimProtectionStat
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
            "freq",
            "def_fgm_per_min",
            "def_fga_per_min",
            "def_fg_pct",
            "points_saved_per_min",
            "def_fg_pct_score",
            "points_saved_per_min_score"
        )
