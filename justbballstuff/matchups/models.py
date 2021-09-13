from django.db import models

# Create your models here.
class Player(models.Model):
    player = models.CharField(max_length=120, blank=False)
    season = models.CharField(max_length=10, blank=False)
    player_id = models.CharField(max_length=50, blank=False)
    team = models.CharField(max_length=3)
    age = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    weight_lb = models.IntegerField(default=0)

    class Meta:
        unique_together = ('player', 'season')

    def get_height(self):
        return f"{int(self.height_in / 12)}'{self.height_in % 12}"

    def __str__(self):
        return f"{self.player} : {self.season}"

class Matchup(models.Model):
    offense_player = models.ForeignKey(Player, related_name='offense_player', on_delete=models.CASCADE)
    defense_player = models.ForeignKey(Player, related_name='defense_player', on_delete=models.CASCADE)
    season = models.CharField(max_length=10, blank=False, verbose_name="SEASON")
    seconds = models.IntegerField(default=0, verbose_name="SECS")
    possessions = models.FloatField(default=0.0, verbose_name="POSS")
    two_pt_made = models.IntegerField(default=0, verbose_name="2PM")
    two_pt_attempt = models.IntegerField(default=0, verbose_name="2PA")
    three_pt_made = models.IntegerField(default=0, verbose_name="3PM")
    three_pt_attempt = models.IntegerField(default=0, verbose_name="3PA")
    free_throw_made = models.IntegerField(default=0, verbose_name="FTM")
    free_throw_attempt = models.IntegerField(default=0, verbose_name="FTA")
    assist = models.IntegerField(default=0, verbose_name="AST")
    turnover = models.IntegerField(default=0, verbose_name="TOV")

    class Meta:
        unique_together = ('offense_player', 'defense_player', 'season')

    def __str__(self):
        return f"{self.offense_player} vs {self.defense_player}"

    def get_mins(self):
        return f"{int(self.seconds / 60)}:{str(self.seconds % 60).zfill(2)}"

    def get_points(self):
        return 2 * self.two_pt_made + 3 * self.three_pt_made + self.free_throw_made

    def get_shot_attempts(self):
        return round(self.two_pt_attempt + self.three_pt_attempt + (0.44 * self.free_throw_attempt), 2)

    def get_eff_field_goal_pct(self):
        return round(100.0 * (self.two_pt_made + 1.5 * self.three_pt_made) / (self.two_pt_attempt + self.three_pt_attempt), 2)

    def get_true_shooting(self):
        return round(100.0 * self.get_points() / (2 * self.get_shot_attempts()), 2)

    def get_three_pt_att_rate(self):
        return round(self.three_pt_attempt / (self.three_pt_attempt + self.two_pt_attempt), 2)

    def get_ftr(self):
        return round(self.free_throw_attempt / (self.three_pt_attempt + self.two_pt_attempt), 2)

    def get_two_pt_pct(self):
        return round(100.0 * (float(self.two_pt_made) / float(self.two_pt_attempt)), 2)

    def get_three_pt_pct(self):
        return round(100.0 * (float(self.three_pt_made) / float(self.three_pt_attempt)), 2)

    def get_free_thow_pct(self):
        return 100.0 * (float(self.free_throw_made) / float(self.free_throw_attempt))

class PlayerStat(models.Model):
    player = models.ForeignKey(Player, related_name='player_stats', on_delete=models.CASCADE)
    season = models.CharField(max_length=10, blank=False)
    poss = models.FloatField(default=0.0)
    usage_score = models.FloatField(default=0.0)
    versatility_score = models.FloatField(default=0.0)
    matchup_height = models.IntegerField(default=0)
    matchup_weight = models.IntegerField(default=0)
    poss_vs_lte75 = models.FloatField(default=0.0)
    poss_vs_lte78 = models.FloatField(default=0.0)
    poss_vs_lte81 = models.FloatField(default=0.0)
    poss_vs_gte82 = models.FloatField(default=0.0)
    freq_vs_lte75 = models.FloatField(default=0.0)
    freq_vs_lte78 = models.FloatField(default=0.0)
    freq_vs_lte81 = models.FloatField(default=0.0)
    freq_vs_gte82 = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('player', 'season')

    def __str__(self):
        return f"{self.player} : {self.season}"
