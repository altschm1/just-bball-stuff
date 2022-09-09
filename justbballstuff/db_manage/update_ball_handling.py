# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from ball_handling.models import BallHandlingStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
BallHandlingStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/ball-handling/final_data/{season_param}/final.csv')
df['dribbles'] = df['Avg\xa0Drib\xa0PerTouch'] * df['TOUCHES']
df['dribbles'] = df['dribbles'].astype('int')
df['backcourt_touches'] = df['TOUCHES'] - df['Front\xa0CTTouches']

rank_cols = ['DRIVES', 'TOUCHES', 'Front\xa0CTTouches', 'Time\xa0OfPoss', 'dribbles', 'ElbowTouches', 'PostUps', 'PaintTouches', 'Turnovers LostBall', 'backcourt_touches']
rank_col_names = ['rank_' + col for col in rank_cols]

for col in rank_cols:
    df['rank_' + col] = df[col] / df['MIN']

df.loc[df['MIN'] < 500, rank_col_names] = np.nan


for col in rank_col_names:
    if col == 'rank_Turnovers LostBall':
        df[col] = df[col].rank(pct=True, ascending=False)
    else:
        df[col] = df[col].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    BallHandlingStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        touches = record['TOUCHES'],
        backcourt_touches = record['backcourt_touches'],
        frontcourt_touches = record['Front\xa0CTTouches'],
        elbow_touches = record['ElbowTouches'],
        post_ups = record['PostUps'],
        paint_touches = record['PaintTouches'],
        drives = record['DRIVES'],
        dribbles = record['dribbles'],
        time_of_poss = record['Time\xa0OfPoss'],
        lost_balls = record['Turnovers LostBall'],
        rank_per_min_touches = 100.0 * record['rank_TOUCHES'],
        rank_per_min_backcourt_touches = 100.0 * record['rank_backcourt_touches'],
        rank_per_min_frontcourt_touches = 100.0 * record['rank_Front\xa0CTTouches'],
        rank_per_min_elbow_touches = 100.0 * record['rank_ElbowTouches'],
        rank_per_min_post_ups = 100.0 * record['rank_PostUps'],
        rank_per_min_paint_touches = 100.0 * record['rank_PaintTouches'],
        rank_per_min_drives = 100.0 * record['rank_DRIVES'],
        rank_per_min_dribbles = 100.0 * record['rank_dribbles'],
        rank_per_min_time_of_poss = 100.0 * record['rank_Time\xa0OfPoss'],
        rank_per_min_lost_balls = 100.0 * record['rank_Turnovers LostBall']
    ) for record in records
]
BallHandlingStat.objects.bulk_create(model_instances)
