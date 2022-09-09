from django.shortcuts import render
from django.apps import apps
from .tables import DefensiveProfileTable, OffensiveProfileTable
from .filters import ProfileFilter
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from heapq import nlargest


PlayerProfile = apps.get_model('matchups', 'Player')

def get_percentile_int(percentile):
    try:
        return int(percentile)
    except:
        return -1

def get_description(score):
    if score is None:
        return None

    if score >= 90:
        return "ELITE"
    elif score >= 65:
        return "GOOD"
    elif score >= 35:
        return "SOLID"
    elif score >= 10:
        return "NOT GOOD"
    else:
        return "BAD"

def get_description_neutral(score):
    if score is None:
        return None

    if score >= 90:
        return "VERY HIGH"
    elif score >= 65:
        return "HIGH"
    elif score >= 35:
        return "AVERAGE"
    elif score >= 10:
        return "LOW"
    else:
        return "VERY LOW"


def get_description_inverse(score):
    if score is None:
        return None

    if score >= 90:
        return "VERY LOW"
    elif score >= 65:
        return "LOW"
    elif score >= 35:
        return "AVERAGE"
    elif score >= 10:
        return "HIGH"
    else:
        return "VERY HIGH"

def get_description_difficulty(score):
    if score is None:
        return None

    if score >= 90:
        return "VERY HARD"
    elif score >= 65:
        return "HARD"
    elif score >= 35:
        return "AVERAGE"
    elif score >= 10:
        return "EASY"
    else:
        return "VERY EASY"

def get_color(score):
    if score is None:
        return None

    if score >= 90:
        return ""
    elif score >= 65:
        return "bg-info"
    elif score >= 35:
        return "bg-success"
    elif score >= 10:
        return "bg-warning"
    else:
        return "bg-danger"


# Create your views here.
class DefenseProfileView(SingleTableMixin, FilterView):
    model = PlayerProfile
    table_class = DefensiveProfileTable
    template_name = 'player_profile/index.html'
    filterset_class = ProfileFilter
    extra_context={'title_head': "Defensive Profiles", "defense" : True}

class OffenseProfileView(SingleTableMixin, FilterView):
    model = PlayerProfile
    table_class = OffensiveProfileTable
    template_name = 'player_profile/index.html'
    filterset_class = ProfileFilter
    extra_context={'title_head': "Offensive Profiles", "offense" : True}

def offense_profile(request, player_id, season):
    PlayerProfile = apps.get_model('matchups', 'Player')
    ScoringStat = apps.get_model('scoring', 'ScoringStat')
    PassingStat = apps.get_model('passing', 'PassingStat')
    BallHandlingStat = apps.get_model('ball_handling', 'BallHandlingStat')
    PlayTypeStat = apps.get_model('playtype', 'PlayTypeStat')
    ShotChartStat = apps.get_model('shot_chart', 'ShotChartStat')
    ShotDifficultyStat = apps.get_model('shot_difficulty', 'ShotDifficultyStat')
    GruntWorkStat = apps.get_model('grunt_work', 'GruntWorkStat')

    player = PlayerProfile.objects.get(player_id=player_id, season=season)
    scorer = ScoringStat.objects.get(player=player.player, season=season)
    passer = PassingStat.objects.get(player=player.player, season=season)
    ball_handler = BallHandlingStat.objects.get(player=player.player, season=season)
    play_type = PlayTypeStat.objects.get(player=player.player, season=season)
    shot_chart = ShotChartStat.objects.get(player=player.player, season=season)
    shot_difficulty = ShotDifficultyStat.objects.get(player=player.player, season=season)
    grunt_work = GruntWorkStat.objects.get(player=player.player, season=season)

    # scoring stats
    points = {'per_36': f"{36.0 * scorer.points / scorer.minutes_played:.2f}", 'percentile': get_percentile_int(scorer.rank_per_min_points), 'desc': get_description(scorer.rank_per_min_points), 'color': get_color(scorer.rank_per_min_points)}
    shot_attempts = {'per_36': f"{36.0 * (scorer.fga + 0.44 * scorer.fta) / scorer.minutes_played:.2f}", 'percentile': get_percentile_int(scorer.rank_per_min_shot_attempts), 'desc': get_description_neutral(scorer.rank_per_min_shot_attempts), 'color': get_color(scorer.rank_per_min_shot_attempts)}
    true_shooting = {'stat': f"{scorer.get_ts():.2f}%", 'percentile': get_percentile_int(scorer.rank_per_min_ts), 'desc': get_description(scorer.rank_per_min_ts), 'color': get_color(scorer.rank_per_min_ts)}

    # passing stats
    assists = {'per_36': f"{36.0 * passer.adj_assists / passer.minutes_played:.2f}", 'percentile': get_percentile_int(passer.rank_per_min_adj_assists), 'desc': get_description(passer.rank_per_min_adj_assists), 'color': get_color(passer.rank_per_min_adj_assists)}
    hockey_assists = {'per_36': f"{36.0 * passer.hockey_assists / passer.minutes_played:.2f}", 'percentile': get_percentile_int(passer.rank_per_min_hockey_assists), 'desc': get_description(passer.rank_per_min_hockey_assists), 'color': get_color(passer.rank_per_min_hockey_assists)}
    potential_assists = {'per_36': f"{36.0 * passer.potential_assists / passer.minutes_played:.2f}", 'percentile': get_percentile_int(passer.rank_per_min_potential_assists), 'desc': get_description(passer.rank_per_min_potential_assists), 'color': get_color(passer.rank_per_min_potential_assists)}
    passes = {'per_36': f"{36.0 * passer.passes / passer.minutes_played:.2f}", 'percentile': get_percentile_int(passer.rank_per_min_passes), 'desc': get_description_neutral(passer.rank_per_min_passes), 'color': get_color(passer.rank_per_min_passes)}
    bad_passes = {'per_36': f"{36.0 * passer.bad_passes / passer.minutes_played:.2f}", 'percentile': get_percentile_int(passer.rank_per_min_bad_passes), 'desc': get_description_inverse(passer.rank_per_min_bad_passes), 'color': get_color(passer.rank_per_min_bad_passes)}

    # ball handling stats
    touches = {'per_36': f"{36.0 * ball_handler.touches / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_touches), 'desc': get_description_neutral(ball_handler.rank_per_min_touches), 'color': get_color(ball_handler.rank_per_min_touches)}
    time_of_poss = {'per_36': f"{36.0 * ball_handler.time_of_poss / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_time_of_poss), 'desc': get_description_neutral(ball_handler.rank_per_min_time_of_poss), 'color': get_color(ball_handler.rank_per_min_time_of_poss)}
    dribbles = {'per_36': f"{36.0 * ball_handler.dribbles / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_dribbles), 'desc': get_description_neutral(ball_handler.rank_per_min_dribbles), 'color': get_color(ball_handler.rank_per_min_dribbles)}
    drives = {'per_36': f"{36.0 * ball_handler.drives / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_drives), 'desc': get_description_neutral(ball_handler.rank_per_min_drives), 'color': get_color(ball_handler.rank_per_min_drives)}
    loose_ball_tov = {'per_36': f"{36.0 * ball_handler.lost_balls / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_lost_balls), 'desc': get_description_inverse(ball_handler.rank_per_min_lost_balls), 'color': get_color(ball_handler.rank_per_min_lost_balls)}
    backcourt_touches = {'per_36': f"{36.0 * ball_handler.backcourt_touches / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_backcourt_touches), 'desc': get_description_neutral(ball_handler.rank_per_min_backcourt_touches), 'color': get_color(ball_handler.rank_per_min_backcourt_touches)}
    frontcourt_touches = {'per_36': f"{36.0 * ball_handler.frontcourt_touches / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_frontcourt_touches), 'desc': get_description_neutral(ball_handler.rank_per_min_frontcourt_touches), 'color': get_color(ball_handler.rank_per_min_frontcourt_touches)}
    elbow_touches = {'per_36': f"{36.0 * ball_handler.elbow_touches / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_elbow_touches), 'desc': get_description_neutral(ball_handler.rank_per_min_elbow_touches), 'color': get_color(ball_handler.rank_per_min_elbow_touches)}
    post_ups = {'per_36': f"{36.0 * ball_handler.post_ups / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_post_ups), 'desc': get_description_neutral(ball_handler.rank_per_min_post_ups), 'color': get_color(ball_handler.rank_per_min_post_ups)}
    paint_touches = {'per_36': f"{36.0 * ball_handler.paint_touches / ball_handler.minutes_played:.2f}", 'percentile': get_percentile_int(ball_handler.rank_per_min_paint_touches), 'desc': get_description_neutral(ball_handler.rank_per_min_paint_touches), 'color': get_color(ball_handler.rank_per_min_paint_touches)}

    # PlayTypeStat
    transition = {'per_36': f"{36.0 * play_type.transition_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_transition_poss), 'desc': get_description_neutral(play_type.rank_per_min_transition_poss), 'color': get_color(play_type.rank_per_min_transition_poss)}
    on_ball_screen = {'per_36': f"{36.0 * play_type.on_ball_screen_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_on_ball_screen_poss), 'desc': get_description_neutral(play_type.rank_per_min_on_ball_screen_poss), 'color': get_color(play_type.rank_per_min_on_ball_screen_poss)}
    one_on_one = {'per_36': f"{36.0 * play_type.one_on_one_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_one_on_one_poss), 'desc': get_description_neutral(play_type.rank_per_min_one_on_one_poss), 'color': get_color(play_type.rank_per_min_one_on_one_poss)}
    off_ball = {'per_36': f"{36.0 * play_type.off_ball_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_off_ball_poss), 'desc': get_description_neutral(play_type.rank_per_min_off_ball_poss), 'color': get_color(play_type.rank_per_min_off_ball_poss)}
    roll = {'per_36': f"{36.0 * play_type.roll_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_roll_poss), 'desc': get_description_neutral(play_type.rank_per_min_roll_poss), 'color': get_color(play_type.rank_per_min_roll_poss)}
    putback = {'per_36': f"{36.0 * play_type.putback_poss / play_type.minutes_played:.2f}", 'percentile': get_percentile_int(play_type.rank_per_min_putback_poss), 'desc': get_description_neutral(play_type.rank_per_min_putback_poss), 'color': get_color(play_type.rank_per_min_putback_poss)}

    # shot charts
    fta = {'per_36': f"{36.0 * shot_chart.fta / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_fta), 'desc': get_description_neutral(shot_chart.rank_per_min_fta), 'color': get_color(shot_chart.rank_per_min_fta)}
    try:
        ft_eff = {'per_36': f"{shot_chart.ft_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_ft_perc), 'desc': get_description(shot_chart.rank_ft_perc), 'color': get_color(shot_chart.rank_ft_perc)}
    except:
        ft_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_ft_perc), 'desc': get_description(shot_chart.rank_ft_perc), 'color': get_color(shot_chart.rank_ft_perc)}
    rim = {'per_36': f"{36.0 * shot_chart.rim_fga / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_rim_fga), 'desc': get_description_neutral(shot_chart.rank_per_min_rim_fga), 'color': get_color(shot_chart.rank_per_min_rim_fga)}
    try:
        rim_eff = {'per_36': f"{shot_chart.rim_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_rim_perc), 'desc': get_description(shot_chart.rank_rim_perc), 'color': get_color(shot_chart.rank_rim_perc)}
    except:
        rim_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_rim_perc), 'desc': get_description(shot_chart.rank_rim_perc), 'color': get_color(shot_chart.rank_rim_perc)}

    floater = {'per_36': f"{36.0 * shot_chart.floater_fga / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_floater_fga), 'desc': get_description_neutral(shot_chart.rank_per_min_floater_fga), 'color': get_color(shot_chart.rank_per_min_floater_fga)}
    try:
        floater_eff = {'per_36': f"{shot_chart.floater_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_floater_perc), 'desc': get_description(shot_chart.rank_floater_perc), 'color': get_color(shot_chart.rank_floater_perc)}
    except:
        floater_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_floater_perc), 'desc': get_description(shot_chart.rank_floater_perc), 'color': get_color(shot_chart.rank_floater_perc)}
    mid = {'per_36': f"{36.0 * shot_chart.midrange_fga / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_midrange_fga), 'desc': get_description_neutral(shot_chart.rank_per_min_midrange_fga), 'color': get_color(shot_chart.rank_per_min_midrange_fga)}
    try:
        mid_eff = {'per_36': f"{shot_chart.midrange_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_midrange_perc), 'desc': get_description(shot_chart.rank_midrange_perc), 'color': get_color(shot_chart.rank_midrange_perc)}
    except:
        mid_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_midrange_perc), 'desc': get_description(shot_chart.rank_midrange_perc), 'color': get_color(shot_chart.rank_midrange_perc)}
    corner = {'per_36': f"{36.0 * shot_chart.corner_fga / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_corner_fga), 'desc': get_description_neutral(shot_chart.rank_per_min_corner_fga), 'color': get_color(shot_chart.rank_per_min_corner_fga)}
    try:
        corner_eff = {'per_36': f"{shot_chart.corner_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_corner_perc), 'desc': get_description(shot_chart.rank_corner_perc), 'color': get_color(shot_chart.rank_corner_perc)}
    except:
        corner_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_corner_perc), 'desc': get_description(shot_chart.rank_corner_perc), 'color': get_color(shot_chart.rank_corner_perc)}
    atb = {'per_36': f"{36.0 * shot_chart.atb_fga / shot_chart.minutes_played:.2f}", 'percentile': get_percentile_int(shot_chart.rank_per_min_atb_fga), 'desc': get_description_neutral(shot_chart.rank_per_min_atb_fga), 'color': get_color(shot_chart.rank_per_min_atb_fga)}
    try:
        atb_eff = {'per_36': f"{shot_chart.atb_perc:.2f}%", 'percentile': get_percentile_int(shot_chart.rank_atb_perc), 'desc': get_description(shot_chart.rank_atb_perc), 'color': get_color(shot_chart.rank_atb_perc)}
    except:
        atb_eff = {'per_36': f"-", 'percentile': get_percentile_int(shot_chart.rank_atb_perc), 'desc': get_description(shot_chart.rank_atb_perc), 'color': get_color(shot_chart.rank_atb_perc)}

    minutes = scorer.minutes_played

    # shot DIFFICULTY
    early_2pa = {'per_36': f"{36.0 * shot_difficulty.early_2pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_early_2pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_early_2pa), 'color': get_color(shot_difficulty.rank_per_min_early_2pa)}
    avg_2pa = {'per_36': f"{36.0 * shot_difficulty.average_2pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_avg_2pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_avg_2pa), 'color': get_color(shot_difficulty.rank_per_min_avg_2pa)}
    late_2pa = {'per_36': f"{36.0 * shot_difficulty.late_2pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_late_2pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_late_2pa), 'color': get_color(shot_difficulty.rank_per_min_late_2pa)}
    early_3pa = {'per_36': f"{36.0 * shot_difficulty.early_3pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_early_3pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_early_3pa), 'color': get_color(shot_difficulty.rank_per_min_early_3pa)}
    avg_3pa = {'per_36': f"{36.0 * shot_difficulty.average_3pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_avg_3pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_avg_3pa), 'color': get_color(shot_difficulty.rank_per_min_avg_3pa)}
    late_3pa = {'per_36': f"{36.0 * shot_difficulty.late_3pa / shot_difficulty.minutes_played:.2f}", 'percentile': get_percentile_int(shot_difficulty.rank_per_min_late_3pa), 'desc': get_description_neutral(shot_difficulty.rank_per_min_late_3pa), 'color': get_color(shot_difficulty.rank_per_min_late_3pa)}
    open_3pa = {'percentile': get_percentile_int(shot_difficulty.rank_open_3pa), 'desc': get_description_difficulty(shot_difficulty.rank_open_3pa), 'color': get_color(shot_difficulty.rank_open_3pa)}
    dribble_2pa = {'percentile': get_percentile_int(shot_difficulty.rank_dribble_2pa), 'desc': get_description_difficulty(shot_difficulty.rank_dribble_2pa), 'color': get_color(shot_difficulty.rank_dribble_2pa)}
    touch_2pa = {'percentile': get_percentile_int(shot_difficulty.rank_touch_2pa), 'desc': get_description_difficulty(shot_difficulty.rank_touch_2pa), 'color': get_color(shot_difficulty.rank_touch_2pa)}

    # grunt WORK
    oreb = {'per_36': f"{36.0 * grunt_work.oreb / grunt_work.minutes_played:.2f}", 'percentile': get_percentile_int(grunt_work.rank_per_min_oreb), 'desc': get_description(grunt_work.rank_per_min_oreb), 'color': get_color(grunt_work.rank_per_min_oreb)}
    screen_assists = {'per_36': f"{36.0 * grunt_work.screen_assists / grunt_work.minutes_played:.2f}", 'percentile': get_percentile_int(grunt_work.rank_per_min_screen_assists), 'desc': get_description(grunt_work.rank_per_min_screen_assists), 'color': get_color(grunt_work.rank_per_min_screen_assists)}
    off_fouls_committed = {'per_36': f"{36.0 * grunt_work.off_fouls_committed / grunt_work.minutes_played:.2f}", 'percentile': get_percentile_int(grunt_work.rank_per_min_off_fouls_committed), 'desc': get_description_inverse(grunt_work.rank_per_min_off_fouls_committed), 'color': get_color(grunt_work.rank_per_min_off_fouls_committed)}
    shooting_fouls_drawn = {'per_36': f"{36.0 * grunt_work.off_fouls_drawn / grunt_work.minutes_played:.2f}", 'percentile': get_percentile_int(grunt_work.rank_per_min_off_fouls_drawn), 'desc': get_description(grunt_work.rank_per_min_off_fouls_drawn), 'color': get_color(grunt_work.rank_per_min_off_fouls_drawn)}

    context = {
        'title_head': f"{str(player)} Offense",
        "offensive_profiles" : True,
        "offense": True,
        'player': player,
        'season': season,
        'minutes': minutes,
        'points': points,
        'shot_attempts': shot_attempts,
        'true_shooting': true_shooting,
        'assists': assists,
        'hockey_assists' : hockey_assists,
        'potential_assists' : potential_assists,
        'passes': passes,
        'bad_passes': bad_passes,
        'touches': touches,
        'time_of_poss': time_of_poss,
        'dribbles': dribbles,
        'drives': drives,
        'loose_ball_tov': loose_ball_tov,
        'backcourt_touches': backcourt_touches,
        'frontcourt_touches': frontcourt_touches,
        'elbow_touches': elbow_touches,
        'post_ups': post_ups,
        'paint_touches': paint_touches,
        'transition': transition,
        'on_ball_screen': on_ball_screen,
        'one_on_one': one_on_one,
        'off_ball': off_ball,
        'roll': roll,
        'putback': putback,
        'fta': fta,
        'ft_eff': ft_eff,
        'rim': rim,
        'rim_eff': rim_eff,
        'floater': floater,
        'floater_eff': floater_eff,
        'mid': mid,
        'mid_eff': mid_eff,
        'corner': corner,
        'corner_eff': corner_eff,
        'atb': atb,
        'atb_eff': atb_eff,
        'early_2pa': early_2pa,
        'avg_2pa': avg_2pa,
        'late_2pa': late_2pa,
        'early_3pa': early_3pa,
        'avg_3pa': avg_3pa,
        'late_3pa': late_3pa,
        'open_3pa': open_3pa,
        'dribble_2pa': dribble_2pa,
        'touch_2pa': touch_2pa,
        'oreb': oreb,
        'screen_assists': screen_assists,
        'off_fouls_committed': off_fouls_committed,
        'shooting_fouls_drawn': shooting_fouls_drawn
    }
    return render(request, 'player_profile/offense_profile.html', context)

def defense_profile(request, player_id, season):
    # get required models
    PlayerProfile = apps.get_model('matchups', 'Player')
    MatchupStats = apps.get_model('matchups', 'PlayerStat')
    RimProtectionStats = apps.get_model('rim_protection', 'RimProtectionStat')
    MatchupBasic = apps.get_model('matchups', 'Matchup')
    Synergy = apps.get_model('defense_synergy', 'DefensiveSynergyStat')
    Playmaking = apps.get_model('defensive_playmaking', 'DefensivePlaymakingStat')
    Rebounding = apps.get_model('defensive_rebounding', 'ReboundingStat')

    player = PlayerProfile.objects.get(player_id=player_id, season=season)
    agg_matchup_stats = MatchupStats.objects.get(player=player, season=season)

    position_keys = dict()
    position_mapping = dict()
    position_mapping['GUARDS'] = "6'3 and shorter"
    position_mapping['WINGS'] = "6'4 to 6'6"
    position_mapping['FORWARDS'] = "6'7 to 6'9"
    position_mapping['BIGS'] = "6'10 and taller"
    position_keys['GUARDS'] = agg_matchup_stats.freq_vs_lte75
    position_keys['WINGS'] = agg_matchup_stats.freq_vs_lte78
    position_keys['FORWARDS'] = agg_matchup_stats.freq_vs_lte81
    position_keys['BIGS'] = agg_matchup_stats.freq_vs_gte82

    position = max(position_keys, key=position_keys.get)
    position_note = f"defends players {position_mapping[position]} {100.0 * position_keys[position]:.2f}% of the time"

    primary_positions = {k: f"defends players {position_mapping[k]} {100.0 * position_keys[k]:.2f}% of the time"  for (k,v) in position_keys.items() if v >= 0.30}
    secondary_positions = {k: f"defends players {position_mapping[k]} {100.0 * position_keys[k]:.2f}% of the time"  for (k,v) in position_keys.items() if v >= 0.15 and v < 0.3}
    no_positions = {k: f"defends players {position_mapping[k]} {100.0 * position_keys[k]:.2f}% of the time"  for (k,v) in position_keys.items() if v < 0.1}

    try:
        rim_protector = RimProtectionStats.objects.get(player=player.player, season=season)
        if rim_protector.freq >= 40.0:
            role = 'Anchor/Low Man'
            role_note = "classified as a F or C by nba.com and at least 40% of shots contested are within 6 feet of the Rim"

        else:
            role = 'Part-time Anchor/Part-time Perimeter Defender'
            role_note = "classified as a F or C by nba.com and between 30 to 40% of shots contested are within 6 feet of the Rim"

        contesting_rim_shots = {'per_36': f"{rim_protector.diff_fg_pct}%",'percentile':  int(rim_protector.diff_fg_pct_score), 'desc': get_description(rim_protector.diff_fg_pct_score), 'color': get_color(rim_protector.diff_fg_pct_score)}

    except:
        role = 'Perimeter Defender'
        role_note = 'classified as a G by nba.com or less than 30% of shots contested are within 6 feet of the Rim'
        contesting_rim_shots = None


    try:
        opposing_matchups = MatchupBasic.objects.filter(defense_player=player).order_by('-possessions').values_list('offense_player__player', flat=True)[0:10]
    except:
        opposing_matchups = []

    matchup_difficulty = {'percentile':  int(agg_matchup_stats.usage_score), 'desc': get_description(agg_matchup_stats.usage_score), 'color': get_color(agg_matchup_stats.usage_score)}
    matchup_versatility = {'percentile':  int(agg_matchup_stats.versatility_score), 'desc': get_description(agg_matchup_stats.versatility_score), 'color': get_color(agg_matchup_stats.versatility_score)}

    playmaker = Playmaking.objects.get(player=player.player, season=season)
    minutes = playmaker.minutes_played
    steals = {'per_36': f"{36.0 * playmaker.steals / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_steals), 'desc': get_description(playmaker.rank_per_min_steals), 'color': get_color(playmaker.rank_per_min_steals)}
    blocks = {'per_36': f"{36.0 * playmaker.blocks / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_blocks), 'desc': get_description(playmaker.rank_per_min_blocks), 'color': get_color(playmaker.rank_per_min_blocks)}
    deflections = {'per_36': f"{36.0 * playmaker.deflections / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_deflections), 'desc': get_description(playmaker.rank_per_min_deflections), 'color': get_color(playmaker.rank_per_min_deflections)}
    stocks = {'per_36': f"{36.0 * (playmaker.steals + playmaker.blocks)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_stocks), 'desc': get_description(playmaker.rank_per_min_stocks), 'color': get_color(playmaker.rank_per_min_stocks)}
    deals = {'per_36': f"{36.0 * (playmaker.steals + playmaker.deflections)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_deals), 'desc': get_description(playmaker.rank_per_min_deals), 'color': get_color(playmaker.rank_per_min_deals)}
    charges = {'per_36': f"{36.0 * (playmaker.charges)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_charges), 'desc': get_description(playmaker.rank_per_min_charges), 'color': get_color(playmaker.rank_per_min_charges)}
    off_fouls_drawn = {'per_36': f"{36.0 * (playmaker.off_fouls_drawn)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_off_fouls_drawn), 'desc': get_description(playmaker.rank_per_min_off_fouls_drawn), 'color': get_color(playmaker.rank_per_min_off_fouls_drawn)}
    shooting_fouls = {'per_36': f"{36.0 * (playmaker.shooting_fouls)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_shooting_fouls), 'desc': get_description_inverse(playmaker.rank_per_min_shooting_fouls), 'color': get_color(playmaker.rank_per_min_shooting_fouls)}

    rebounder = Rebounding.objects.get(player=player.player, season=season)
    dreb = {'per_36': f"{rebounder.dreb_per_min:.2f}",'percentile':  int(rebounder.dreb_rank_per_min), 'desc': get_description(rebounder.dreb_rank_per_min), 'color': get_color(rebounder.dreb_rank_per_min)}
    boxouts = {'per_36': f"{rebounder.dboxout_per_min:.2f}",'percentile':  int(rebounder.dboxout_rank_per_min), 'desc': get_description(rebounder.dboxout_rank_per_min), 'color': get_color(rebounder.dboxout_rank_per_min)}

    context = {
        'title_head': f"{str(player)} Defense",
        "defensive_profiles" : True,
        "defense": True,
        'player': player,
        'season': season,
        'poss': agg_matchup_stats.poss,
        'opp_height': f"{int(agg_matchup_stats.matchup_height / 12)}'{agg_matchup_stats.matchup_height % 12}",
        'opp_weight': agg_matchup_stats.matchup_weight,
        'position': position,
        'position_note': position_note,
        'primary_positions': primary_positions,
        'secondary_positions': secondary_positions,
        'no_positions': no_positions,
        'role': role,
        'role_note': role_note,
        'opposing_matchups': opposing_matchups,
        "matchup_difficulty": matchup_difficulty,
        'matchup_versatility': matchup_versatility,
        'steals': steals,
        'blocks': blocks,
        'deflections': deflections,
        'stocks': stocks,
        'deals': deals,
        'charges': charges,
        'off_fouls_drawn': off_fouls_drawn,
        'shooting_fouls': shooting_fouls,
        'dreb': dreb,
        'boxouts': boxouts,
        'contesting_rim_shots': contesting_rim_shots,
        'minutes': minutes
    }
    return render(request, 'player_profile/defense_profile.html', context)
