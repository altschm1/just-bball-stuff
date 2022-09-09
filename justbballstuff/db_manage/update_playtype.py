# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from playtype.models import PlayTypeStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
PlayTypeStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/synergy/final_data/{season_param}/offense.csv')
num = df._get_numeric_data()
print(num)
for col in num.columns:
    if 'poss' in col:
        print(col)
        df[col] = df[col].fillna(0)
        df.loc[df[col] < 0, [col]] = 0

df['on_ball_screen_poss'] = df['ball-handler_poss'] + df['hand-off_poss']
df['one_on_one_poss'] = df['isolation_poss'] + df['playtype-post-up_poss']
df['off_ball_poss'] = df['spot-up_poss'] + df['cut_poss'] + df['off-screen_poss']

rank_cols = ['on_ball_screen_poss', 'one_on_one_poss', 'off_ball_poss', 'transition_poss', 'roll-man_poss', 'putbacks_poss']
rank_col_names = ['rank_' + col for col in rank_cols]

for col in rank_cols:
    df['rank_' + col] = df[col] / df['MIN']

df.loc[df['MIN'] < 500, rank_col_names] = np.nan


for col in rank_col_names:
    df[col] = df[col].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    PlayTypeStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        transition_poss = record['transition_poss'],
        on_ball_screen_poss = record['on_ball_screen_poss'],
        one_on_one_poss = record['one_on_one_poss'],
        off_ball_poss = record['off_ball_poss'],
        roll_poss = record['roll-man_poss'],
        putback_poss = record['putbacks_poss'],
        rank_per_min_transition_poss = 100.0 * record['rank_transition_poss'],
        rank_per_min_on_ball_screen_poss = 100.0 * record['rank_on_ball_screen_poss'],
        rank_per_min_one_on_one_poss = 100.0 * record['rank_one_on_one_poss'],
        rank_per_min_off_ball_poss = 100.0 * record['rank_off_ball_poss'],
        rank_per_min_roll_poss = 100.0 * record['rank_roll-man_poss'],
        rank_per_min_putback_poss = 100.0 * record['rank_putbacks_poss']
    ) for record in records
]
PlayTypeStat.objects.bulk_create(model_instances)
