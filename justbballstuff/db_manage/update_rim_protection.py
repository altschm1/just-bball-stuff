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
df['DFG% RANK'] = df['DFG%']
df['Diff% RANK'] = df['Diff%']
df.loc[df['MIN'] < 500, ['DFG% RANK', 'Diff% RANK']] = np.nan
df['DFG% RANK'] = df['DFG% RANK'].rank(pct=True, ascending=False)
df['Diff% RANK'] = df['Diff% RANK'].rank(pct=True, ascending=False)

df['DFGM_game'] = df['DFGM'] / df['GP']
df['DFGA_game'] = df['DFGA'] / df['GP']

df['DFGM_min'] = 36.0 * df['DFGM'] / df['MIN']
df['DFGA_min'] = 36.0 * df['DFGA'] / df['MIN']
df.fillna(-1, inplace=True)


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
        diff_fg_pct =record['Diff%'],
        def_fg_pct_score = 100.0 * record['DFG% RANK'],
        diff_fg_pct_score = 100.0 * record['Diff% RANK'],
        def_fgm_per_game = record['DFGM_game'],
        def_fga_per_game = record['DFGA_game'],
        def_fgm_per_min = record['DFGM_min'],
        def_fga_per_min = record['DFGA_min'],
    ) for record in records
]
RimProtectionStat.objects.bulk_create(model_instances)
