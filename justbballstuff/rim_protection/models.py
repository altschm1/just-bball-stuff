from django.db import models

# Create your models here.
class RimProtectionStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    freq = models.FloatField(default=0.0)
    def_fgm = models.IntegerField(default=0)
    def_fga = models.IntegerField(default=0)
    def_fg_pct = models.FloatField(default=0.0)
    points_saved = models.FloatField(default=0.0)
    def_fg_pct_score = models.FloatField(default=0.0, null=True)
    points_saved_score = models.FloatField(default=0.0, null=True)
    def_fgm_per_game = models.FloatField(default=0.0)
    def_fga_per_game = models.FloatField(default=0.0)
    points_saved_per_game = models.FloatField(default=0.0)
    points_saved_per_game_score = models.FloatField(default=0.0, null=True)
    def_fgm_per_min = models.FloatField(default=0.0)
    def_fga_per_min = models.FloatField(default=0.0)
    points_saved_per_min = models.FloatField(default=0.0)
    points_saved_per_min_score = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
