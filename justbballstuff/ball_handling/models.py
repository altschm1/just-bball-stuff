from django.db import models

# Create your models here.
class BallHandlingStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    touches = models.IntegerField(default=0)
    backcourt_touches = models.IntegerField(default=0)
    frontcourt_touches = models.IntegerField(default=0)
    elbow_touches = models.IntegerField(default=0)
    post_ups = models.IntegerField(default=0)
    paint_touches = models.IntegerField(default=0)
    drives = models.IntegerField(default=0)
    dribbles = models.IntegerField(default=0)
    time_of_poss = models.IntegerField(default=0)
    lost_balls = models.IntegerField(default=0)

    rank_per_min_touches = models.FloatField(default=0.0, null=True)
    rank_per_min_backcourt_touches = models.FloatField(default=0.0, null=True)
    rank_per_min_frontcourt_touches = models.FloatField(default=0.0, null=True)
    rank_per_min_elbow_touches = models.FloatField(default=0.0, null=True)
    rank_per_min_post_ups = models.FloatField(default=0.0, null=True)
    rank_per_min_paint_touches = models.FloatField(default=0.0, null=True)
    rank_per_min_drives = models.FloatField(default=0.0, null=True)
    rank_per_min_dribbles = models.FloatField(default=0.0, null=True)
    rank_per_min_time_of_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_lost_balls = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
