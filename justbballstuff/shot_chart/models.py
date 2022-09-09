from django.db import models

# Create your models here.
class ShotChartStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    fta = models.IntegerField(default=0)
    rim_fga = models.IntegerField(default=0)
    floater_fga = models.IntegerField(default=0)
    midrange_fga = models.IntegerField(default=0)
    corner_fga = models.IntegerField(default=0)
    atb_fga = models.IntegerField(default=0)
    ft_perc = models.FloatField(default=0.0, null=True)
    rim_perc = models.FloatField(default=0.0, null=True)
    floater_perc = models.FloatField(default=0.0, null=True)
    midrange_perc = models.FloatField(default=0.0, null=True)
    corner_perc = models.FloatField(default=0.0, null=True)
    atb_perc = models.FloatField(default=0.0, null=True)

    rank_per_min_fta = models.FloatField(default=0.0, null=True)
    rank_per_min_rim_fga = models.FloatField(default=0.0, null=True)
    rank_per_min_floater_fga = models.FloatField(default=0.0, null=True)
    rank_per_min_midrange_fga = models.FloatField(default=0.0, null=True)
    rank_per_min_corner_fga = models.FloatField(default=0.0, null=True)
    rank_per_min_atb_fga = models.FloatField(default=0.0, null=True)
    rank_ft_perc = models.FloatField(default=0.0, null=True)
    rank_rim_perc = models.FloatField(default=0.0, null=True)
    rank_floater_perc = models.FloatField(default=0.0, null=True)
    rank_midrange_perc = models.FloatField(default=0.0, null=True)
    rank_corner_perc = models.FloatField(default=0.0, null=True)
    rank_atb_perc = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
