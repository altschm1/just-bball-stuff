import django_tables2 as tables
from .models import DefensiveSynergyStat
from django.db.models import F, FloatField
from django.db.models.functions import Cast

class TotalDefensiveSynergyTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    isolation_poss = tables.Column(verbose_name="Iso Poss", accessor="isolation_poss")
    isolation_ppp = tables.Column(verbose_name="Iso PPP", accessor="isolation_ppp")
    ball_handler_poss = tables.Column(verbose_name="PnR BH Poss", accessor="ball_handler_poss")
    ball_handler_ppp = tables.Column(verbose_name="PnR BH PPP", accessor="ball_handler_ppp")
    roll_man_poss = tables.Column(verbose_name="PnR Screener Poss", accessor="roll_man_poss")
    roll_man_ppp = tables.Column(verbose_name="PnR Screener PPP", accessor="roll_man_ppp")
    post_up_poss = tables.Column(verbose_name="Post-up Poss", accessor="post_up_poss")
    post_up_ppp = tables.Column(verbose_name="Post-up PPP", accessor="post_up_ppp")
    spot_up_poss = tables.Column(verbose_name="Spot-up Poss", accessor="spot_up_poss")
    spot_up_ppp = tables.Column(verbose_name="Spot-up PPP", accessor="spot_up_ppp")
    hand_off_poss = tables.Column(verbose_name="Hand-off Poss", accessor="hand_off_poss")
    hand_off_ppp = tables.Column(verbose_name="Hand-off PPP", accessor="hand_off_ppp")
    off_screen_poss = tables.Column(verbose_name="Off-screen Poss", accessor="off_screen_poss")
    off_screen_ppp = tables.Column(verbose_name="Off-screen PPP", accessor="off_screen_ppp")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_isolation_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_isolation_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_ball_handler_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_ball_handler_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_roll_man_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_roll_man_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_post_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_post_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_spot_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_spot_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_hand_off_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_hand_off_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_off_screen_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return value

    def render_off_screen_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    class Meta:
        model = DefensiveSynergyStat
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
            "isolation_poss",
            "isolation_ppp",
            "ball_handler_poss",
            "ball_handler_ppp",
            "roll_man_poss",
            "roll_man_ppp",
            "post_up_poss",
            "post_up_ppp",
            "spot_up_poss",
            "spot_up_ppp",
            "hand_off_poss",
            "hand_off_ppp",
            "off_screen_poss",
            "off_screen_ppp",
        )

class PerGameDefensiveSynergyTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    isolation_poss = tables.Column(verbose_name="Iso Poss", accessor="isolation_poss")
    isolation_ppp = tables.Column(verbose_name="Iso PPP", accessor="isolation_ppp")
    ball_handler_poss = tables.Column(verbose_name="PnR BH Poss", accessor="ball_handler_poss")
    ball_handler_ppp = tables.Column(verbose_name="PnR BH PPP", accessor="ball_handler_ppp")
    roll_man_poss = tables.Column(verbose_name="PnR Screener Poss", accessor="roll_man_poss")
    roll_man_ppp = tables.Column(verbose_name="PnR Screener PPP", accessor="roll_man_ppp")
    post_up_poss = tables.Column(verbose_name="Post-up Poss", accessor="post_up_poss")
    post_up_ppp = tables.Column(verbose_name="Post-up PPP", accessor="post_up_ppp")
    spot_up_poss = tables.Column(verbose_name="Spot-up Poss", accessor="spot_up_poss")
    spot_up_ppp = tables.Column(verbose_name="Spot-up PPP", accessor="spot_up_ppp")
    hand_off_poss = tables.Column(verbose_name="Hand-off Poss", accessor="hand_off_poss")
    hand_off_ppp = tables.Column(verbose_name="Hand-off PPP", accessor="hand_off_ppp")
    off_screen_poss = tables.Column(verbose_name="Off-screen Poss", accessor="off_screen_poss")
    off_screen_ppp = tables.Column(verbose_name="Off-screen PPP", accessor="off_screen_ppp")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_isolation_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_isolation_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_ball_handler_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_ball_handler_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_roll_man_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_roll_man_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_post_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_post_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_spot_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_spot_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_hand_off_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_hand_off_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_off_screen_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{float(value) / float(record.games_played):.2f}"

    def render_off_screen_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def order_isolation_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            iso_poss = Cast("isolation_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "iso_poss")
        return (queryset, True)

    def order_ball_handler_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            bh_poss = Cast("ball_handler_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "bh_poss")
        return (queryset, True)

    def order_roll_man_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            screener_poss = Cast("roll_man_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "screener_poss")
        return (queryset, True)

    def order_post_up_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            post_poss = Cast("post_up_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "post_poss")
        return (queryset, True)

    def order_spot_up_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            spot_poss = Cast("spot_up_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "spot_poss")
        return (queryset, True)

    def order_hand_off_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            dho_poss = Cast("hand_off_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "dho_poss")
        return (queryset, True)

    def order_off_screen_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            os_poss = Cast("off_screen_poss", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "os_poss")
        return (queryset, True)

    class Meta:
        model = DefensiveSynergyStat
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
            "isolation_poss",
            "isolation_ppp",
            "ball_handler_poss",
            "ball_handler_ppp",
            "roll_man_poss",
            "roll_man_ppp",
            "post_up_poss",
            "post_up_ppp",
            "spot_up_poss",
            "spot_up_ppp",
            "hand_off_poss",
            "hand_off_ppp",
            "off_screen_poss",
            "off_screen_ppp",
        )

class PerMinDefensiveSynergyTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    isolation_poss = tables.Column(verbose_name="Iso Poss", accessor="isolation_poss")
    isolation_ppp = tables.Column(verbose_name="Iso PPP", accessor="isolation_ppp")
    ball_handler_poss = tables.Column(verbose_name="PnR BH Poss", accessor="ball_handler_poss")
    ball_handler_ppp = tables.Column(verbose_name="PnR BH PPP", accessor="ball_handler_ppp")
    roll_man_poss = tables.Column(verbose_name="PnR Screener Poss", accessor="roll_man_poss")
    roll_man_ppp = tables.Column(verbose_name="PnR Screener PPP", accessor="roll_man_ppp")
    post_up_poss = tables.Column(verbose_name="Post-up Poss", accessor="post_up_poss")
    post_up_ppp = tables.Column(verbose_name="Post-up PPP", accessor="post_up_ppp")
    hand_off_poss = tables.Column(verbose_name="Hand-off Poss", accessor="hand_off_poss")
    hand_off_ppp = tables.Column(verbose_name="Hand-off PPP", accessor="hand_off_ppp")
    off_screen_poss = tables.Column(verbose_name="Off-screen Poss", accessor="off_screen_poss")
    off_screen_ppp = tables.Column(verbose_name="Off-screen PPP", accessor="off_screen_ppp")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_isolation_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_isolation_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_ball_handler_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_ball_handler_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_roll_man_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_roll_man_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_post_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_post_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_spot_up_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_spot_up_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_hand_off_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_hand_off_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"

    def render_off_screen_poss(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_off_screen_ppp(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{value:.2f}"


    def order_isolation_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            iso_poss = 36.0 * Cast("isolation_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "iso_poss")
        return (queryset, True)

    def order_ball_handler_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            bh_poss = 36.0 * Cast("ball_handler_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "bh_poss")
        return (queryset, True)

    def order_roll_man_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            screener_poss = 36.0 * Cast("roll_man_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "screener_poss")
        return (queryset, True)

    def order_post_up_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            post_poss = 36.0 * Cast("post_up_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "post_poss")
        return (queryset, True)

    def order_hand_off_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            dho_poss = 36.0 * Cast("hand_off_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "dho_poss")
        return (queryset, True)

    def order_off_screen_poss(self, queryset, is_descending):
        queryset = queryset.annotate(
            os_poss = 36.0 * Cast("off_screen_poss", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "os_poss")
        return (queryset, True)

    class Meta:
        model = DefensiveSynergyStat
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
            "isolation_poss",
            "isolation_ppp",
            "ball_handler_poss",
            "ball_handler_ppp",
            "roll_man_poss",
            "roll_man_ppp",
            "post_up_poss",
            "post_up_ppp",
            "spot_up_poss",
            "spot_up_ppp",
            "hand_off_poss",
            "hand_off_ppp",
            "off_screen_poss",
            "off_screen_ppp",
        )

class SummaryDefensiveSynergyTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    isolation_freq = tables.Column(verbose_name="Iso Freq%", accessor="isolation_freq")
    isolation_percentile = tables.Column(verbose_name="Iso Percentile", accessor="isolation_percentile")
    ball_handler_freq = tables.Column(verbose_name="PnR BH Freq%", accessor="ball_handler_freq")
    ball_handler_percentile = tables.Column(verbose_name="PnR BH Percentile", accessor="ball_handler_percentile")
    roll_man_freq = tables.Column(verbose_name="PnR Screener Freq%", accessor="roll_man_freq")
    roll_man_percentile = tables.Column(verbose_name="PnR Screener Percentile", accessor="roll_man_percentile")
    post_up_freq = tables.Column(verbose_name="Post-up Freq%", accessor="post_up_freq")
    post_up_percentile = tables.Column(verbose_name="Post-up Percentile", accessor="post_up_percentile")
    spot_up_freq = tables.Column(verbose_name="Spot-up Freq%", accessor="spot_up_freq")
    spot_up_percentile = tables.Column(verbose_name="Spot-up Percentile", accessor="spot_up_percentile")
    hand_off_freq = tables.Column(verbose_name="Hand-off Freq%", accessor="hand_off_freq")
    hand_off_percentile = tables.Column(verbose_name="Hand-off Percentile", accessor="hand_off_percentile")
    off_screen_freq = tables.Column(verbose_name="Off-screen Freq%", accessor="off_screen_freq")
    off_screen_percentile = tables.Column(verbose_name="Off-screen Percentile", accessor="off_screen_percentile")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_isolation_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_isolation_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_ball_handler_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_ball_handler_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_roll_man_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_roll_man_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_post_up_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_post_up_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_spot_up_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_spot_up_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_hand_off_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_hand_off_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_off_screen_freq(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    def render_off_screen_percentile(self, value, record):
        if value < 0:
            return '-'
        else:
            return f"{100.0 * value:.2f}%"

    class Meta:
        model = DefensiveSynergyStat
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
            "isolation_freq",
            "isolation_percentile",
            "ball_handler_freq",
            "ball_handler_percentile",
            "roll_man_freq",
            "roll_man_percentile",
            "post_up_freq",
            "post_up_percentile",
            "spot_up_freq",
            "spot_up_percentile",
            "hand_off_freq",
            "hand_off_percentile",
            "off_screen_freq",
            "off_screen_percentile",
        )
