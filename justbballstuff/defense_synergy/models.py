from django.db import models

# Create your models here.
class DefensiveSynergyStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    isolation_poss = models.IntegerField(default=0)
    isolation_pts = models.IntegerField(default=0)
    isolation_percentile = models.FloatField(default=0.0)
    isolation_ppp = models.FloatField(default=0.0)
    isolation_freq = models.FloatField(default=0.0)
    ball_handler_poss = models.IntegerField(default=0)
    ball_handler_pts = models.IntegerField(default=0)
    ball_handler_percentile = models.FloatField(default=0.0)
    ball_handler_ppp = models.FloatField(default=0.0)
    ball_handler_freq = models.FloatField(default=0.0)
    roll_man_poss = models.IntegerField(default=0)
    roll_man_pts = models.IntegerField(default=0)
    roll_man_percentile = models.FloatField(default=0.0)
    roll_man_ppp = models.FloatField(default=0.0)
    roll_man_freq = models.FloatField(default=0.0)
    post_up_poss = models.IntegerField(default=0)
    post_up_pts = models.IntegerField(default=0)
    post_up_percentile = models.FloatField(default=0.0)
    post_up_ppp = models.FloatField(default=0.0)
    post_up_freq = models.FloatField(default=0.0)
    spot_up_poss = models.IntegerField(default=0)
    spot_up_pts = models.IntegerField(default=0)
    spot_up_percentile = models.FloatField(default=0.0)
    spot_up_ppp = models.FloatField(default=0.0)
    spot_up_freq = models.FloatField(default=0.0)
    hand_off_poss = models.IntegerField(default=0)
    hand_off_pts = models.IntegerField(default=0)
    hand_off_percentile = models.FloatField(default=0.0)
    hand_off_ppp = models.FloatField(default=0.0)
    hand_off_freq = models.FloatField(default=0.0)
    off_screen_poss = models.IntegerField(default=0)
    off_screen_pts = models.IntegerField(default=0)
    off_screen_percentile = models.FloatField(default=0.0)
    off_screen_ppp = models.FloatField(default=0.0)
    off_screen_freq = models.FloatField(default=0.0)


    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
