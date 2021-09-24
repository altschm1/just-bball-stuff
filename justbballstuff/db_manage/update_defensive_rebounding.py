# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from defensive_rebounding.models import ReboundingStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
ReboundingStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/dreb/final_data/{season_param}/final.csv')
df['dreb_game'] = df['DREB'] / df['GP']
df['def_box_out_game'] = df['DEF Box Outs'] / df['GP']
df['dreb_min'] = 36.0 * df['DREB'] / df['MIN']
df['def_box_out_min'] = 36.0 * df['DEF Box Outs'] / df['MIN']

df['dreb_rank'] = df['DREB']
df['def_box_out_rank'] = df['DEF Box Outs']
df['dreb_rank_game'] = df['dreb_game']
df['def_box_out_rank_game'] = df['def_box_out_game']
df['dreb_rank_min'] = df['dreb_min']
df['def_box_out_rank_min'] = df['def_box_out_min']
df.loc[df['MIN'] < 500, ['dreb_rank', 'def_box_out_rank', 'dreb_rank_game', 'def_box_out_rank_game', 'dreb_rank_min', 'def_box_out_rank_min']] = np.nan
df['dreb_rank'] = 100.0 * df['dreb_rank'].rank(pct=True)
df['def_box_out_rank'] = 100.0 * df['def_box_out_rank'].rank(pct=True)
df['dreb_rank_game'] = 100.0 * df['dreb_rank_game'].rank(pct=True)
df['def_box_out_rank_game'] = 100.0 * df['def_box_out_rank_game'].rank(pct=True)
df['dreb_rank_min'] = 100.0 * df['dreb_rank_min'].rank(pct=True)
df['def_box_out_rank_min'] = 100.0 * df['def_box_out_rank_min'].rank(pct=True)
df = df.fillna(-100)

print(df)

records = df.to_dict('records')
model_instances = [
    ReboundingStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        dreb = record['DREB'],
        dboxout = record['DEF Box Outs'],
        dreb_rank = record['dreb_rank'],
        dboxout_rank = record['def_box_out_rank'],
        dreb_per_game = record['dreb_game'],
        dboxout_per_game = record['def_box_out_game'],
        dreb_rank_per_game = record['dreb_rank_game'],
        dboxout_rank_per_game = record['def_box_out_rank_game'],
        dreb_per_min = record['dreb_min'],
        dboxout_per_min = record['def_box_out_min'],
        dreb_rank_per_min = record['dreb_rank_min'],
        dboxout_rank_per_min = record['def_box_out_rank_min'],
    ) for record in records
]
ReboundingStat.objects.bulk_create(model_instances)
