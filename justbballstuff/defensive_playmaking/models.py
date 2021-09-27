from django.db import models

# Create your models here.
class DefensivePlaymakingStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    deflections = models.IntegerField(default=0)
    charges = models.IntegerField(default=0)
    off_fouls_drawn = models.IntegerField(default=0)
    shooting_fouls = models.IntegerField(default=0)

    rank_per_game_steals = models.FloatField(default=0.0, null=True)
    rank_per_game_blocks = models.FloatField(default=0.0, null=True)
    rank_per_game_deflections = models.FloatField(default=0.0, null=True)
    rank_per_game_stocks = models.FloatField(default=0.0, null=True)
    rank_per_game_deals = models.FloatField(default=0.0, null=True)
    rank_per_game_charges = models.FloatField(default=0.0, null=True)
    rank_per_game_off_fouls_drawn = models.FloatField(default=0.0, null=True)
    rank_per_game_shooting_fouls = models.FloatField(default=0.0, null=True)

    rank_per_min_steals = models.FloatField(default=0.0, null=True)
    rank_per_min_blocks = models.FloatField(default=0.0, null=True)
    rank_per_min_deflections = models.FloatField(default=0.0, null=True)
    rank_per_min_stocks = models.FloatField(default=0.0, null=True)
    rank_per_min_deals = models.FloatField(default=0.0, null=True)
    rank_per_min_charges = models.FloatField(default=0.0, null=True)
    rank_per_min_off_fouls_drawn = models.FloatField(default=0.0, null=True)
    rank_per_min_shooting_fouls = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def get_deals(self):
        return self.steals + self.deflections

    def get_stocks(self):
        return self.steals + self.blocks

    def __str__(self):
        return f"{self.player} : {self.season}"
