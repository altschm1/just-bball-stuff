# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from matchups.models import Player, PlayerStat, Matchup
import pandas as pd

season_param = sys.argv[1]

# drop all the data for season_param
Player.objects.filter(season=season_param).delete()
Matchup.objects.filter(season=season_param).delete()
PlayerStat.objects.filter(season=season_param).delete()

# update Player model
df = pd.read_csv(f'C:/Users/18562/matchup-data/nba-matchup-data/final_data/{season_param}/players.csv')
records = df.to_dict('records')
model_instances = [
    Player(
        player = record['player'],
        season = record['season'],
        player_id = record['slug'],
        team = record['team'],
        age = record['age'],
        height_in = record['height_in'],
        weight_lb = record['weight_lb']
    ) for record in records
]
Player.objects.bulk_create(model_instances)


# create mapping from player to season to Player objects
player_mapping = dict()
for r in records:
    player_mapping[f"{r['player']}|{r['season']}"] = Player.objects.get(player=r['player'], season=r['season'])

# update Matchup model
df = pd.read_csv(f'C:/Users/18562/matchup-data/nba-matchup-data/final_data/{season_param}/matchups.csv')
records = df.to_dict('records')
model_instances = [
    Matchup(
        offense_player = player_mapping[f"{r['offense_player']}|{r['SEASON']}"],
        defense_player = player_mapping[f"{r['defense_player']}|{r['SEASON']}"],
        season = r['SEASON'],
        seconds = r['SECS'],
        possessions = r['POSS'],
        two_pt_made = r['2PM'],
        two_pt_attempt = r['2PA'],
        three_pt_made = r['3PM'],
        three_pt_attempt = r['3PA'],
        free_throw_made = r['FTM'],
        free_throw_attempt = r['FTA'],
        assist = r['AST'],
        turnover = r['TOV']
    ) for r in records
]
Matchup.objects.bulk_create(model_instances)

# update PlayerStat Model
df = pd.read_csv(f'C:/Users/18562/matchup-data/nba-matchup-data/final_data/{season_param}/stats.csv')
records = df.to_dict('records')
model_instances = [
    PlayerStat(
        player = player_mapping[f"{r['player']}|{r['season']}"],
        season = r['season'],
        poss =r['POSS'],
        usage_score = 100.0 * r['adj_usg_rank'],
        versatility_score = 100.0 * r['versatility_score_rank'],
        matchup_height = int(r['height']),
        matchup_weight = int(r['weight']),
        poss_vs_lte75 = r['poss_lte75'],
        poss_vs_lte78 = r['poss_lte78'],
        poss_vs_lte81 = r['poss_lte81'],
        poss_vs_gte82 = r['poss_gte82'],
        freq_vs_lte75 = r['freq_lte75'],
        freq_vs_lte78 = r['freq_lte78'],
        freq_vs_lte81 = r['freq_lte81'],
        freq_vs_gte82 = r['freq_gte82']
    ) for r in records
]
PlayerStat.objects.bulk_create(model_instances)
