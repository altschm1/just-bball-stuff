from django.db import models

# Create your models here.
class ReboundingStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    dreb = models.IntegerField(default=0)
    dboxout = models.IntegerField(default=0)
    dreb_rank = models.FloatField(default=0.0)
    dboxout_rank = models.FloatField(default=0.0)
    dreb_per_game = models.FloatField(default=0.0)
    dboxout_per_game = models.FloatField(default=0.0)
    dreb_rank_per_game = models.FloatField(default=0.0)
    dboxout_rank_per_game = models.FloatField(default=0.0)
    dreb_per_min = models.FloatField(default=0.0)
    dboxout_per_min = models.FloatField(default=0.0)
    dreb_rank_per_min = models.FloatField(default=0.0)
    dboxout_rank_per_min = models.FloatField(default=0.0)


    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
