# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from rim_protection.models import RimProtectionStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
RimProtectionStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/rim-protection/final_data/{season_param}/final.csv')
df['DFG%'] = 100.0 * df['DFGM'] / df['DFGA']
df['PTS SAVED'] = 2 * (df['DFGM'] - ((df['FG%']/100.0) * df['DFGA']))
df['DFG% RANK'] = df['DFG%']
df['PTS SAVED RANK'] = df['PTS SAVED']
df.loc[df['MIN'] < 500, ['DFG% RANK', 'PTS SAVED RANK']] = np.nan
df['DFG% RANK'] = df['DFG% RANK'].rank(pct=True, ascending=False)
df['PTS SAVED RANK'] = df['PTS SAVED RANK'].rank(pct=True, ascending=False)

df['DFGM_game'] = df['DFGM'] / df['GP']
df['DFGA_game'] = df['DFGA'] / df['GP']
df['PTS SAVED GAME'] = 2 * (df['DFGM_game'] - ((df['FG%']/100.0) * df['DFGA_game']))
df['PTS SAVED GAME RANK'] = df['PTS SAVED GAME']
df.loc[df['MIN'] < 500, ['PTS SAVED GAME RANK']] = np.nan
df['PTS SAVED GAME RANK'] = df['PTS SAVED GAME RANK'].rank(pct=True, ascending=False)

df['DFGM_min'] = 36.0 * df['DFGM'] / df['MIN']
df['DFGA_min'] = 36.0 * df['DFGA'] / df['MIN']
df['PTS SAVED MIN'] = 2 * (df['DFGM_min'] - ((df['FG%']/100.0) * df['DFGA_min']))
df['PTS SAVED MIN RANK'] = df['PTS SAVED MIN']
df.loc[df['MIN'] < 500, ['PTS SAVED MIN RANK']] = np.nan
df['PTS SAVED MIN RANK'] = df['PTS SAVED MIN RANK'].rank(pct=True, ascending=False)

print(df)

records = df.to_dict('records')
model_instances = [
    RimProtectionStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        freq = float(record['FREQ'].split('%')[0]),
        def_fgm = record['DFGM'],
        def_fga = record['DFGA'],
        def_fg_pct = record['DFG%'],
        points_saved =record['PTS SAVED'],
        def_fg_pct_score = 100.0 * record['DFG% RANK'],
        points_saved_score = 100.0 * record['PTS SAVED RANK'],
        def_fgm_per_game = record['DFGM_game'],
        def_fga_per_game = record['DFGA_game'],
        points_saved_per_game = record['PTS SAVED GAME'],
        points_saved_per_game_score = 100.0 * record['PTS SAVED GAME RANK'],
        def_fgm_per_min = record['DFGM_min'],
        def_fga_per_min = record['DFGA_min'],
        points_saved_per_min = record['PTS SAVED MIN'],
        points_saved_per_min_score = 100.0 * record['PTS SAVED MIN RANK']
    ) for record in records
]
RimProtectionStat.objects.bulk_create(model_instances)
