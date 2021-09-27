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
df['charges_game'] = df['ChargesDrawn'] / df['GP']
#df['other_off_fouls_game'] = (df['Fouls Drawn Off.'] - df['ChargesDrawn']) / df['GP']
df['off_fouls_game'] = df['Fouls Drawn Off.'] / df['GP']
df['shooting_fouls_game'] = df['Fouls Committed Shoot'] / df['GP']
df.loc[df['MIN'] < 500, ['stl_game', 'blk_game', 'defl_game', 'stk_game', 'deal_game', 'charges_game', 'off_fouls_game', 'shooting_fouls_game']] = np.nan
df['stl_game'] = df['stl_game'].rank(pct=True)
df['blk_game'] = df['blk_game'].rank(pct=True)
df['defl_game'] = df['defl_game'].rank(pct=True)
df['stk_game'] = df['stk_game'].rank(pct=True)
df['deal_game'] = df['deal_game'].rank(pct=True)
df['charges_game'] = df['charges_game'].rank(pct=True)
#df['other_off_fouls_game'] = df['other_off_fouls_game'].rank(pct=True)
df['off_fouls_game'] = df['off_fouls_game'].rank(pct=True)
df['shooting_fouls_game'] = df['shooting_fouls_game'].rank(pct=True, ascending=False)

df['stl_min'] = df['STL'] / df['MIN']
df['blk_min'] = df['BLK'] / df['MIN']
df['defl_min'] = df['Deflections'] / df['MIN']
df['stk_min'] = df['stocks'] / df['MIN']
df['deal_min'] = df['deals'] / df['MIN']
df['charges_min'] = df['ChargesDrawn'] / df['MIN']
#df['other_off_fouls_min'] = (df['Fouls Drawn Off.'] - df['ChargesDrawn']) / df['MIN']
df['off_fouls_min'] = df['Fouls Drawn Off.'] / df['MIN']
df['shooting_fouls_min'] = df['Fouls Committed Shoot'] / df['MIN']
df.loc[df['MIN'] < 500, ['stl_min', 'blk_min', 'defl_min', 'stk_min', 'deal_min', 'charges_min', 'off_fouls_min', 'shooting_fouls_min']] = np.nan
df['stl_min'] = df['stl_min'].rank(pct=True)
df['blk_min'] = df['blk_min'].rank(pct=True)
df['defl_min'] = df['defl_min'].rank(pct=True)
df['stk_min'] = df['stk_min'].rank(pct=True)
df['deal_min'] = df['deal_min'].rank(pct=True)
df['charges_min'] = df['charges_min'].rank(pct=True)
#df['other_off_fouls_min'] = df['other_off_fouls_min'].rank(pct=True)
df['off_fouls_min'] = df['off_fouls_min'].rank(pct=True)
df['shooting_fouls_min'] = df['shooting_fouls_min'].rank(pct=True, ascending=False)
df.fillna({'stl_game':-1, 'blk_game':-1, 'defl_game':-1, 'stk_game':-1, 'deal_game':-1, 'charges_game':-1, 'off_fouls_game':-1, 'shooting_fouls_game':-1}, inplace=True)
df.fillna({'stl_min':-1, 'blk_min':-1, 'defl_min':-1, 'stk_min':-1, 'deal_min':-1, 'charges_min':-1, 'off_fouls_min':-1, 'shooting_fouls_min':-1}, inplace=True)

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
        charges = record['ChargesDrawn'],
        off_fouls_drawn = record['Fouls Drawn Off.'],
        shooting_fouls = record['Fouls Committed Shoot'],
        rank_per_game_steals = 100.0 * record['stl_game'],
        rank_per_game_blocks = 100.0 * record['blk_game'],
        rank_per_game_deflections = 100.0 * record['defl_game'],
        rank_per_game_stocks = 100.0 * record['stk_game'],
        rank_per_game_deals = 100.0 * record['deal_game'],
        rank_per_game_charges = 100.0 * record['charges_game'],
        rank_per_game_off_fouls_drawn = 100.0 * record['off_fouls_game'],
        rank_per_game_shooting_fouls = 100.0 * record['shooting_fouls_game'],
        rank_per_min_steals = 100.0 * record['stl_min'],
        rank_per_min_blocks = 100.0 * record['blk_min'],
        rank_per_min_deflections = 100.0 * record['defl_min'],
        rank_per_min_stocks = 100.0 * record['stk_min'],
        rank_per_min_deals = 100.0 * record['deal_min'],
        rank_per_min_charges = 100.0 * record['charges_min'],
        rank_per_min_off_fouls_drawn = 100.0 * record['off_fouls_min'],
        rank_per_min_shooting_fouls = 100.0 * record['shooting_fouls_min'],
    ) for record in records
]
DefensivePlaymakingStat.objects.bulk_create(model_instances)
