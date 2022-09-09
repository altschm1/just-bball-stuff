from django.db import models

# Create your models here.
class PassingStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    passes = models.IntegerField(default=0)
    adj_assists = models.IntegerField(default=0)
    hockey_assists = models.IntegerField(default=0)
    potential_assists = models.IntegerField(default=0)
    bad_passes = models.IntegerField(default=0)

    rank_per_min_passes = models.FloatField(default=0.0, null=True)
    rank_per_min_adj_assists = models.FloatField(default=0.0, null=True)
    rank_per_min_hockey_assists = models.FloatField(default=0.0, null=True)
    rank_per_min_potential_assists = models.FloatField(default=0.0, null=True)
    rank_per_min_bad_passes = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
