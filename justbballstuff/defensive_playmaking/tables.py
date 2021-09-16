import django_tables2 as tables
from .models import DefensivePlaymakingStat
from django.db.models import F, FloatField
from django.db.models.functions import Cast

class TotalDefensivePlaymakingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    steals = tables.Column(verbose_name="STL", accessor="steals")
    blocks = tables.Column(verbose_name="BLK", accessor="blocks")
    deflections = tables.Column(verbose_name="DEFLECTIONS", accessor="deflections")
    deals = tables.Column(verbose_name="DEALS", accessor="get_deals")
    stocks = tables.Column(verbose_name="STOCKS", accessor="get_stocks")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def order_deals(self, queryset, is_descending):
        queryset = queryset.annotate(
            deals = F("steals") + F("deflections")
        ).order_by(("-" if is_descending else "") + "deals")
        return (queryset, True)

    def order_stocks(self, queryset, is_descending):
        queryset = queryset.annotate(
            stocks = F("steals") + F("blocks")
        ).order_by(("-" if is_descending else "") + "stocks")
        return (queryset, True)


    class Meta:
        model = DefensivePlaymakingStat
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
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )

class PerGameDefensivePlaymakingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    steals = tables.Column(verbose_name="STL", accessor="steals")
    blocks = tables.Column(verbose_name="BLK", accessor="blocks")
    deflections = tables.Column(verbose_name="DEFLECTIONS", accessor="deflections")
    deals = tables.Column(verbose_name="DEALS", accessor="get_deals")
    stocks = tables.Column(verbose_name="STOCKS", accessor="get_stocks")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def order_deals(self, queryset, is_descending):
        queryset = queryset.annotate(
            deals = (Cast("steals", FloatField()) + Cast("deflections", FloatField())) / (Cast("games_played", FloatField()))
        ).order_by(("-" if is_descending else "") + "deals")
        return (queryset, True)

    def order_stocks(self, queryset, is_descending):
        queryset = queryset.annotate(
            stocks = (Cast("steals", FloatField()) + Cast("blocks", FloatField())) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "stocks")
        return (queryset, True)

    def order_steals(self, queryset, is_descending):
        queryset = queryset.annotate(
            stls = Cast("steals", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "stls")
        return (queryset, True)

    def order_blocks(self, queryset, is_descending):
        queryset = queryset.annotate(
            blks = Cast("blocks", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "blks")
        return (queryset, True)

    def order_deflections(self, queryset, is_descending):
        queryset = queryset.annotate(
            defl = Cast("deflections", FloatField()) / Cast("games_played", FloatField())
        ).order_by(("-" if is_descending else "") + "defl")
        return (queryset, True)

    def render_steals(self, value, record):
        return f"{float(value) / float(record.games_played):.2f}"

    def render_blocks(self, value, record):
        return f"{float(value) / float(record.games_played):.2f}"

    def render_deflections(self, value, record):
        return f"{float(value) / float(record.games_played):.2f}"

    def render_stocks(self, value, record):
        return f"{float(value) / float(record.games_played):.2f}"

    def render_deals(self, value, record):
        return f"{float(value) / float(record.games_played):.2f}"


    class Meta:
        model = DefensivePlaymakingStat
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
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )

class PerMinDefensivePlaymakingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    steals = tables.Column(verbose_name="STL", accessor="steals")
    blocks = tables.Column(verbose_name="BLK", accessor="blocks")
    deflections = tables.Column(verbose_name="DEFLECTIONS", accessor="deflections")
    deals = tables.Column(verbose_name="DEALS", accessor="get_deals")
    stocks = tables.Column(verbose_name="STOCKS", accessor="get_stocks")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def order_deals(self, queryset, is_descending):
        queryset = queryset.annotate(
            deals = 36.0 * (Cast("steals", FloatField()) + Cast("deflections", FloatField())) / (Cast("minutes_played", FloatField()))
        ).order_by(("-" if is_descending else "") + "deals")
        return (queryset, True)

    def order_stocks(self, queryset, is_descending):
        queryset = queryset.annotate(
            stocks = 36.0 * (Cast("steals", FloatField()) + Cast("blocks", FloatField())) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "stocks")
        return (queryset, True)

    def order_steals(self, queryset, is_descending):
        queryset = queryset.annotate(
            stls = 36.0 * Cast("steals", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "stls")
        return (queryset, True)

    def order_blocks(self, queryset, is_descending):
        queryset = queryset.annotate(
            blks = 36.0* Cast("blocks", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "blks")
        return (queryset, True)

    def order_deflections(self, queryset, is_descending):
        queryset = queryset.annotate(
            defl = 36.0 * Cast("deflections", FloatField()) / Cast("minutes_played", FloatField())
        ).order_by(("-" if is_descending else "") + "defl")
        return (queryset, True)

    def render_steals(self, value, record):
        return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_blocks(self, value, record):
        return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_deflections(self, value, record):
        return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_stocks(self, value, record):
        return f"{36.0 * float(value) / float(record.minutes_played):.2f}"

    def render_deals(self, value, record):
        return f"{36.0 * float(value) / float(record.minutes_played):.2f}"


    class Meta:
        model = DefensivePlaymakingStat
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
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )

class RankPerGameDefensivePlaymakingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    steals = tables.Column(verbose_name="STL", accessor="rank_per_game_steals")
    blocks = tables.Column(verbose_name="BLK", accessor="rank_per_game_blocks")
    deflections = tables.Column(verbose_name="DEFLECTIONS", accessor="rank_per_game_deflections")
    deals = tables.Column(verbose_name="DEALS", accessor="rank_per_game_deals")
    stocks = tables.Column(verbose_name="STOCKS", accessor="rank_per_game_stocks")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_steals(self, value, record):
        return f"{float(value):.2f}"

    def render_blocks(self, value, record):
        return f"{float(value):.2f}"

    def render_deflections(self, value, record):
        return f"{float(value):.2f}"

    def render_stocks(self, value, record):
        return f"{float(value):.2f}"

    def render_deals(self, value, record):
        return f"{float(value):.2f}"


    class Meta:
        model = DefensivePlaymakingStat
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
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )

class RankPerMinDefensivePlaymakingTable(tables.Table):
    player = tables.Column(verbose_name="PLAYER", accessor='player')
    team = tables.Column(verbose_name="TEAM", accessor='team')
    age = tables.Column(verbose_name="AGE", accessor='age')
    height_in = tables.Column(verbose_name="HEIGHT", accessor='get_height', order_by="height_in")
    weight_lb = tables.Column(verbose_name="WEIGHT", accessor='weight_lb')
    season = tables.Column(verbose_name="SEASON", accessor="season")
    games_played = tables.Column(verbose_name="GP", accessor="games_played")
    minutes_played = tables.Column(verbose_name="MP", accessor="minutes_played")
    steals = tables.Column(verbose_name="STL", accessor="rank_per_min_steals")
    blocks = tables.Column(verbose_name="BLK", accessor="rank_per_min_blocks")
    deflections = tables.Column(verbose_name="DEFLECTIONS", accessor="rank_per_min_deflections")
    deals = tables.Column(verbose_name="DEALS", accessor="rank_per_min_deals")
    stocks = tables.Column(verbose_name="STOCKS", accessor="rank_per_min_stocks")

    def render_weight_lb(self, value, record):
        return str(value) + " lb"

    def render_steals(self, value, record):
        return f"{float(value):.2f}"

    def render_blocks(self, value, record):
        return f"{float(value):.2f}"

    def render_deflections(self, value, record):
        return f"{float(value):.2f}"

    def render_stocks(self, value, record):
        return f"{float(value):.2f}"

    def render_deals(self, value, record):
        return f"{float(value):.2f}"


    class Meta:
        model = DefensivePlaymakingStat
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
            "steals",
            "blocks",
            "deflections",
            "stocks",
            "deals",
        )
