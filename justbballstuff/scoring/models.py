from django.db import models

# Create your models here.
class ScoringStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    points = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    fta = models.IntegerField(default=0)

    rank_per_min_points = models.FloatField(default=0.0, null=True)
    rank_per_min_shot_attempts = models.FloatField(default=0.0, null=True)
    rank_per_min_ts = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def get_shot_attempts(self):
        return round(self.fga + (0.44 * self.fta), 2)

    def get_ts(self):
        return round(100.0 * self.points / (2 * self.get_shot_attempts()), 2)

    def __str__(self):
        return f"{self.player} : {self.season}"
