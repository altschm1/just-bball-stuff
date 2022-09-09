from django.db import models

# Create your models here.
class PlayTypeStat(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)

    transition_poss = models.IntegerField(default=0)
    on_ball_screen_poss = models.IntegerField(default=0)
    one_on_one_poss = models.IntegerField(default=0)
    off_ball_poss = models.IntegerField(default=0)
    roll_poss = models.IntegerField(default=0)
    putback_poss = models.IntegerField(default=0)

    rank_per_min_transition_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_on_ball_screen_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_one_on_one_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_off_ball_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_roll_poss = models.FloatField(default=0.0, null=True)
    rank_per_min_putback_poss = models.FloatField(default=0.0, null=True)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"
