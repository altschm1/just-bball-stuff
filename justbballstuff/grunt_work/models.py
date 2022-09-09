from django.db import models

# Create your models here.
class GruntWorkStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    oreb = models.IntegerField(default=0)
    screen_assists = models.IntegerField(default=0)
    off_fouls_committed = models.IntegerField(default=0)
    off_fouls_drawn = models.IntegerField(default=0)

    rank_per_min_oreb = models.FloatField(default=0.0, null=True)
    rank_per_min_screen_assists = models.FloatField(default=0.0, null=True)
    rank_per_min_off_fouls_committed = models.FloatField(default=0.0, null=True)
    rank_per_min_off_fouls_drawn = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
