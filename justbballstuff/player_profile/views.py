from django.shortcuts import render
from django.apps import apps
from .tables import ProfileTable
from .filters import ProfileFilter
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from heapq import nlargest


PlayerProfile = apps.get_model('matchups', 'Player')

def get_description(score):
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

def get_color(score):
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
class ProfileView(SingleTableMixin, FilterView):
    model = PlayerProfile
    table_class = ProfileTable
    template_name = 'player_profile/index.html'
    filterset_class = ProfileFilter
    extra_context={'title_head': "Defensive Profiles", "profiles" : True, "defense": True}

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
            role = 'Primary Rim Protector/Low Man'
            role_note = "classified as a F or C by nba.com and at least 40% of shots contested are within 6 feet of the Rim"

        else:
            role = 'Secondary Rim Protector/Perimeter Big/Sinker'
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

    try:
        synergy_stats = Synergy.objects.get(player=player.player, season=season)
        playtype_mapping = dict()
        playtype_mapping["isolations"] = synergy_stats.isolation_poss
        playtype_mapping['pick n roll ball handler'] = synergy_stats.ball_handler_poss
        playtype_mapping['pick n roll screener'] = synergy_stats.roll_man_poss
        playtype_mapping['post ups'] = synergy_stats.post_up_poss
        playtype_mapping['spot ups'] = synergy_stats.spot_up_poss
        playtype_mapping['hand offs'] = synergy_stats.hand_off_poss
        playtype_mapping['off screens'] = synergy_stats.off_screen_poss
        top_3_synergy = nlargest(3, playtype_mapping, key = playtype_mapping.get)
    except:
        top_3_synergy = []


    matchup_difficulty = {'percentile':  int(agg_matchup_stats.usage_score), 'desc': get_description(agg_matchup_stats.usage_score), 'color': get_color(agg_matchup_stats.usage_score)}
    matchup_versatility = {'percentile':  int(agg_matchup_stats.versatility_score), 'desc': get_description(agg_matchup_stats.versatility_score), 'color': get_color(agg_matchup_stats.versatility_score)}

    playmaker = Playmaking.objects.get(player=player.player, season=season)
    steals = {'per_36': f"{36.0 * playmaker.steals / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_steals), 'desc': get_description(playmaker.rank_per_min_steals), 'color': get_color(playmaker.rank_per_min_steals)}
    blocks = {'per_36': f"{36.0 * playmaker.blocks / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_blocks), 'desc': get_description(playmaker.rank_per_min_blocks), 'color': get_color(playmaker.rank_per_min_blocks)}
    deflections = {'per_36': f"{36.0 * playmaker.deflections / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_deflections), 'desc': get_description(playmaker.rank_per_min_deflections), 'color': get_color(playmaker.rank_per_min_deflections)}
    stocks = {'per_36': f"{36.0 * (playmaker.steals + playmaker.blocks)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_stocks), 'desc': get_description(playmaker.rank_per_min_stocks), 'color': get_color(playmaker.rank_per_min_stocks)}
    deals = {'per_36': f"{36.0 * (playmaker.steals + playmaker.deflections)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_deals), 'desc': get_description(playmaker.rank_per_min_deals), 'color': get_color(playmaker.rank_per_min_deals)}
    charges = {'per_36': f"{36.0 * (playmaker.charges)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_charges), 'desc': get_description(playmaker.rank_per_min_charges), 'color': get_color(playmaker.rank_per_min_charges)}
    off_fouls_drawn = {'per_36': f"{36.0 * (playmaker.off_fouls_drawn)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_off_fouls_drawn), 'desc': get_description(playmaker.rank_per_min_off_fouls_drawn), 'color': get_color(playmaker.rank_per_min_off_fouls_drawn)}
    shooting_fouls = {'per_36': f"{36.0 * (playmaker.shooting_fouls)  / playmaker.minutes_played:.2f}",'percentile':  int(playmaker.rank_per_min_shooting_fouls), 'desc': get_description(playmaker.rank_per_min_shooting_fouls), 'color': get_color(playmaker.rank_per_min_shooting_fouls)}

    rebounder = Rebounding.objects.get(player=player.player, season=season)
    dreb = {'per_36': f"{rebounder.dreb_per_min:.2f}",'percentile':  int(rebounder.dreb_rank_per_min), 'desc': get_description(rebounder.dreb_rank_per_min), 'color': get_color(rebounder.dreb_rank_per_min)}
    boxouts = {'per_36': f"{rebounder.dboxout_per_min:.2f}",'percentile':  int(rebounder.dboxout_rank_per_min), 'desc': get_description(rebounder.dboxout_rank_per_min), 'color': get_color(rebounder.dboxout_rank_per_min)}

    context = {
        'title_head': f"{str(player)} Defense",
        "profiles" : True,
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
        'top_synergy': top_3_synergy,
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
        'contesting_rim_shots': contesting_rim_shots
    }
    return render(request, 'player_profile/profile.html', context)
