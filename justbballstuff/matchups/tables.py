import django_tables2 as tables
from .models import Matchup, PlayerStat
from django_tables2.utils import A
from django.db.models import F

class MatchupTable(tables.Table):
    mins = tables.Column(verbose_name="MINS", order_by="seconds", accessor=A('get_mins'))
    off_player = tables.Column(verbose_name="OFF PLAYER", accessor='offense_player.player')
    off_team = tables.Column(verbose_name="OFF TEAM", accessor='offense_player.team')
    off_age = tables.Column(verbose_name="OFF AGE", accessor='offense_player.age')
    off_height = tables.Column(verbose_name="OFF HEIGHT", accessor='offense_player.get_height', order_by="offense_player.height_in")
    off_weight = tables.Column(verbose_name="OFF WEIGHT", accessor='offense_player.weight_lb')
    def_player = tables.Column(verbose_name="DEF PLAYER", accessor='defense_player.player')
    def_team = tables.Column(verbose_name="DEF TEAM", accessor='defense_player.team')
    def_age = tables.Column(verbose_name="DEF AGE", accessor='defense_player.age')
    def_height = tables.Column(verbose_name="DEF HEIGHT", accessor='defense_player.get_height', order_by="defense_player.height_in")
    def_weight = tables.Column(verbose_name="DEF WEIGHT", accessor='defense_player.weight_lb')
    pts = tables.Column(verbose_name="PTS", accessor=A('get_points'))
    two_pt_pct = tables.Column(verbose_name="2P%", accessor=A('get_two_pt_pct'))
    three_pt_pct = tables.Column(verbose_name="3P%", accessor=A('get_three_pt_pct'))
    shot_attempts = tables.Column(verbose_name="SHOT ATTEMPTS*", accessor=A('get_shot_attempts'))
    efg = tables.Column(verbose_name="eFG%", accessor=A('get_eff_field_goal_pct'))
    ts = tables.Column(verbose_name="TS%", accessor=A('get_true_shooting'))
    three_pt_att_rate = tables.Column(verbose_name="3PAr", accessor=A('get_three_pt_att_rate'))
    ftr = tables.Column(verbose_name="FTr", accessor=A('get_ftr'))

    def render_off_weight(self, value, record):
        return str(value) + " lb"

    def render_def_weight(self, value, record):
        return str(value) + " lb"

    def order_pts(self, queryset, is_descending):
        queryset = queryset.annotate(
            pts = 2 * F("two_pt_made") + 3 * F("three_pt_made") + F("free_throw_made")
        ).order_by(("-" if is_descending else "") + "pts")
        return (queryset, True)

    def order_shot_attempts(self, queryset, is_descending):
        queryset = queryset.annotate(
            shots = F("two_pt_attempt") + F("three_pt_attempt") + 0.44 * F("free_throw_attempt")
        ).order_by(("-" if is_descending else "") + "shots")
        return (queryset, True)

    def order_two_pt_pct(self, queryset, is_descending):
        queryset = queryset.annotate(
            two_pt_pct = 100.0 * F("two_pt_made") / F("two_pt_attempt")
        ).order_by(("-" if is_descending else "") + "two_pt_pct")
        return (queryset, True)

    def order_three_pt_pct(self, queryset, is_descending):
        queryset = queryset.annotate(
            three_pt_pct = 100.0 * F("three_pt_made") / F("three_pt_attempt")
        ).order_by(("-" if is_descending else "") + "three_pt_pct")
        return (queryset, True)

    def order_efg(self, queryset, is_descending):
        queryset = queryset.annotate(
            efg = (F("two_pt_made") + 1.5 * F("three_pt_made")) / (0.001 + F("two_pt_attempt") + F("three_pt_attempt"))
        ).order_by(("-" if is_descending else "") + "efg")
        return (queryset, True)

    def order_ts(self, queryset, is_descending):
        queryset = queryset.annotate(
            ts = (2 * F("two_pt_made") + 3 * F("three_pt_made") + F("free_throw_made")) / (2 * (0.001 + F("two_pt_attempt") + F("three_pt_attempt") + 0.44 * F("free_throw_attempt")))
        ).order_by(("-" if is_descending else "") + "ts")
        return (queryset, True)

    def order_three_pt_att_rate(self, queryset, is_descending):
        queryset = queryset.annotate(
            three_att_rate = F("two_pt_attempt") / (0.001 + F("three_pt_attempt") + F("two_pt_attempt"))
        ).order_by(("-" if is_descending else "") + "three_att_rate")
        return (queryset, True)

    def order_ftr(self, queryset, is_descending):
        queryset = queryset.annotate(
            ftr = F("free_throw_attempt") / (0.001 + F("two_pt_attempt") + F("three_pt_attempt"))
        ).order_by(("-" if is_descending else "") + "ftr")
        return (queryset, True)


    class Meta:
        model = Matchup
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "off_player",
            'off_team',
            "off_age",
            "off_height",
            "off_weight",
            "def_player",
            'def_team',
            "def_age",
            "def_height",
            "def_weight",
            "season",
            "mins",
            "possessions",
            "pts",
            "shot_attempts",
            "two_pt_made",
            "two_pt_attempt",
            "two_pt_pct",
            "three_pt_made",
            "three_pt_attempt",
            "three_pt_pct",
            "free_throw_made",
            "free_throw_attempt",
            "assist",
            "turnover",
            "efg",
            "ts",
            "three_pt_att_rate",
            "ftr"
        )


class StatTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player.player')
    team = tables.Column(verbose_name="TEAM", accessor='player.team')
    age = tables.Column(verbose_name="AGE", accessor='player.age')
    height = tables.Column(verbose_name="HEIGHT", accessor='player.get_height', order_by="player.height_in")
    weight = tables.Column(verbose_name="WEIGHT", accessor='player.weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    poss = tables.Column(verbose_name="POSS", accessor="poss")
    usage_score = tables.Column(verbose_name="USG SCORE", accessor="usage_score")
    versatility_score = tables.Column(verbose_name="VERSATILITY SCORE", accessor="versatility_score")
    matchup_height = tables.Column(verbose_name="AVG MATCHUP HEIGHT", accessor="matchup_height")
    matchup_weight = tables.Column(verbose_name="AVG MATCHUP WEIGHT", accessor="matchup_weight")
    poss_vs_lte75 = tables.Column(verbose_name="POSS <= 6'3", accessor="poss_vs_lte75")
    poss_vs_lte78 = tables.Column(verbose_name="POSS 6'4 to 6'6", accessor="poss_vs_lte78")
    poss_vs_lte81 = tables.Column(verbose_name="POSS 6'7 to 6'9", accessor="poss_vs_lte81")
    poss_vs_gte82 = tables.Column(verbose_name="POSS >= 6'10", accessor="poss_vs_gte82")
    freq_vs_lte75 = tables.Column(verbose_name="FREQ <= 6'3", accessor="freq_vs_lte75")
    freq_vs_lte78 = tables.Column(verbose_name="FREQ 6'4 to 6'6", accessor="freq_vs_lte78")
    freq_vs_lte81 = tables.Column(verbose_name="FREQ 6'7 to 6'9", accessor="freq_vs_lte81")
    freq_vs_gte82 = tables.Column(verbose_name="FREQ >= 6'10", accessor="freq_vs_gte82")

    def render_weight(self, value, record):
        return str(value) + " lb"

    def render_poss(self, value, record):
        return round(value, 2)

    def render_usage_score(self, value, record):
        return "{0:.2f}".format(value)

    def render_versatility_score(self, value, record):
        return "{0:.2f}".format(value)

    def render_matchup_height(self, value, record):
        return f"{int(value / 12)}'{value % 12}"

    def render_poss_vs_lte75(self, value, record):
        return round(value, 2)

    def render_poss_vs_lte78(self, value, record):
        return round(value, 2)

    def render_poss_vs_lte81(self, value, record):
        return round(value, 2)

    def render_poss_vs_gte82(self, value, record):
        return round(value, 2)

    def render_freq_vs_lte75(self, value, record):
        return "{0:.2f}%".format(100.0 * value)

    def render_freq_vs_lte78(self, value, record):
        return "{0:.2f}%".format(100.0 * value)

    def render_freq_vs_lte81(self, value, record):
        return "{0:.2f}%".format(100.0 * value)

    def render_freq_vs_gte82(self, value, record):
        return "{0:.2f}%".format(100.0 * value)




    class Meta:
        model = PlayerStat
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-striped"}
        fields = (
            "player",
            'team',
            "age",
            "height",
            "weight",
            "season",
            "poss",
            "usage_score",
            "versatility_score",
            "matchup_height",
            "matchup_weight",
            "poss_vs_lte75",
            "poss_vs_lte78",
            "poss_vs_lte81",
            "poss_vs_gte82",
            "freq_vs_lte75",
            "freq_vs_lte78",
            "freq_vs_lte81",
            "freq_vs_gte82"
        )
