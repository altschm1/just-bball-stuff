# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from scoring.models import ScoringStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
ScoringStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/scoring/final_data/{season_param}/final.csv')
df['points_per_min'] = df['PTS'] / df['MIN']
df['shots_per_min'] = (df['FGA'] + 0.44 * df['FTA']) / df['MIN']
df['ts%'] =  100.0 * df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))

df.loc[df['MIN'] < 500, ['points_per_min', 'shots_per_min', 'ts%']] = np.nan

df['points_per_min'] = df['points_per_min'].rank(pct=True)
df['shots_per_min'] = df['shots_per_min'].rank(pct=True)
df['ts%'] = df['ts%'].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    ScoringStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        points = record['PTS'],
        fga = record['FGA'],
        fta = record['FTA'],
        rank_per_min_points = 100.0 * record['points_per_min'],
        rank_per_min_shot_attempts = 100.0 * record['shots_per_min'],
        rank_per_min_ts = 100.0 * record['ts%']
    ) for record in records
]
ScoringStat.objects.bulk_create(model_instances)
