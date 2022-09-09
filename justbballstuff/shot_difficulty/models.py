from django.db import models

# Create your models here.
class ShotDifficultyStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    early_2pa = models.IntegerField(default=0)
    average_2pa = models.IntegerField(default=0)
    late_2pa = models.IntegerField(default=0)
    early_3pa = models.IntegerField(default=0)
    average_3pa = models.IntegerField(default=0)
    late_3pa = models.IntegerField(default=0)

    rank_per_min_early_2pa = models.FloatField(default=0.0, null=True)
    rank_per_min_early_3pa = models.FloatField(default=0.0, null=True)
    rank_per_min_avg_2pa = models.FloatField(default=0.0, null=True)
    rank_per_min_avg_3pa = models.FloatField(default=0.0, null=True)
    rank_per_min_late_2pa = models.FloatField(default=0.0, null=True)
    rank_per_min_late_3pa = models.FloatField(default=0.0, null=True)
    rank_open_3pa = models.FloatField(default=0.0, null=True)
    rank_touch_2pa = models.FloatField(default=0.0, null=True)
    rank_dribble_2pa = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
