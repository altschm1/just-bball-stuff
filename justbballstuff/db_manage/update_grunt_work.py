# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from grunt_work.models import GruntWorkStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
GruntWorkStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/grunt-work/final_data/{season_param}/final.csv')

rank_cols = ['OREB', 'ScreenAssists', 'Fouls Drawn Shoot', 'Fouls Committed Off.']
rank_col_names = ['rank_' + col for col in rank_cols]

for col in rank_cols:
    df['rank_' + col] = df[col] / df['MIN']

df.loc[df['MIN'] < 500, rank_col_names] = np.nan


for col in rank_col_names:
    if col == 'rank_Fouls Committed Off.':
        df[col] = df[col].rank(pct=True, ascending=False)
    else:
        df[col] = df[col].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    GruntWorkStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        oreb = record['OREB'],
        screen_assists = record['ScreenAssists'],
        off_fouls_committed = record['Fouls Committed Off.'],
        off_fouls_drawn = record['Fouls Drawn Shoot'],
        rank_per_min_oreb = 100.0 * record['rank_OREB'],
        rank_per_min_screen_assists = 100.0 * record['rank_ScreenAssists'],
        rank_per_min_off_fouls_committed = 100.0 * record['rank_Fouls Committed Off.'],
        rank_per_min_off_fouls_drawn = 100.0 * record['rank_Fouls Drawn Shoot']
    ) for record in records
]
GruntWorkStat.objects.bulk_create(model_instances)
