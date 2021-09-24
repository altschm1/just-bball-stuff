# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from defensive_playmaking.models import DefensivePlaymakingStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
DefensivePlaymakingStat.objects.filter(season=season_param).delete()

# update Player model
df = pd.read_csv(f'C:/Users/18562/defense-playmaking/final_data/{season_param}/final.csv')
df['stocks'] = df['STL'] + df['BLK']
df['deals'] = df['STL'] + df['Deflections']
df['stl_game'] = df['STL'] / df['GP']
df['blk_game'] = df['BLK'] / df['GP']
df['defl_game'] = df['Deflections'] / df['GP']
df['stk_game'] = df['stocks'] / df['GP']
df['deal_game'] = df['deals'] / df['GP']
df.loc[df['MIN'] < 500, ['stl_game', 'blk_game', 'defl_game', 'stk_game', 'deal_game']] = np.nan
df['stl_game'] = df['stl_game'].rank(pct=True)
df['blk_game'] = df['blk_game'].rank(pct=True)
df['defl_game'] = df['defl_game'].rank(pct=True)
df['stk_game'] = df['stk_game'].rank(pct=True)
df['deal_game'] = df['deal_game'].rank(pct=True)

df['stl_min'] = df['STL'] / df['MIN']
df['blk_min'] = df['BLK'] / df['MIN']
df['defl_min'] = df['Deflections'] / df['MIN']
df['stk_min'] = df['stocks'] / df['MIN']
df['deal_min'] = df['deals'] / df['MIN']
df.loc[df['MIN'] < 500, ['stl_min', 'blk_min', 'defl_min', 'stk_min', 'deal_min']] = np.nan
df['stl_min'] = df['stl_min'].rank(pct=True)
df['blk_min'] = df['blk_min'].rank(pct=True)
df['defl_min'] = df['defl_min'].rank(pct=True)
df['stk_min'] = df['stk_min'].rank(pct=True)
df['deal_min'] = df['deal_min'].rank(pct=True)
df.fillna({'stl_game':-1, 'blk_game':-1, 'defl_game':-1, 'stk_game':-1, 'deal_game':-1}, inplace=True)
df.fillna({'stl_min':-1, 'blk_min':-1, 'defl_min':-1, 'stk_min':-1, 'deal_min':-1}, inplace=True)

print(df)
records = df.to_dict('records')
model_instances = [
    DefensivePlaymakingStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        steals = record['STL'],
        blocks = record['BLK'],
        deflections = record['Deflections'],
        rank_per_game_steals = 100.0 * record['stl_game'],
        rank_per_game_blocks = 100.0 * record['blk_game'],
        rank_per_game_deflections = 100.0 * record['defl_game'],
        rank_per_game_stocks = 100.0 * record['stk_game'],
        rank_per_game_deals = 100.0 * record['deal_game'],
        rank_per_min_steals = 100.0 * record['stl_min'],
        rank_per_min_blocks = 100.0 * record['blk_min'],
        rank_per_min_deflections = 100.0 * record['defl_min'],
        rank_per_min_stocks = 100.0 * record['stk_min'],
        rank_per_min_deals = 100.0 * record['deal_min']
    ) for record in records
]
DefensivePlaymakingStat.objects.bulk_create(model_instances)
