# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from shot_difficulty.models import ShotDifficultyStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
ShotDifficultyStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/shot-difficulty/final_data/{season_param}/final.csv')

df.fillna(0, inplace=True)

df['early_2pa'] = df['24-22 sec 2PA'] + df['22-18 sec 2PA'] + df['18-15 sec 2PA']
df['avg_2pa'] = df['15-7 sec 2PA']
df['late_2pa'] = df['7-4 sec 2PA'] + df['4-0 sec 2PA']
df['early_3pa'] = df['24-22 sec 3PA'] + df['22-18 sec 3PA'] + df['18-15 sec 3PA']
df['avg_3pa'] = df['15-7 sec 3PA']
df['late_3pa'] = df['7-4 sec 3PA'] + df['4-0 sec 3PA']
df['open_3pt_rtg'] = (1 * df['0-2ft 3PA'] + 3 * df['2-4ft 3PA'] + 5 * df['4-6ft 3PA'] + 7 * df['6+ft 3PA']) / (df['0-2ft 3PA'] + df['2-4ft 3PA'] + df['4-6ft 3PA'] + df['6+ft 3PA'])
df['dribble_2pt_rtg'] = (0 * df['0 dribble 2PA'] + 1 * df['1 dribble 2PA'] + 2 * df['2 dribble 2PA'] + 4.5 * df['3-6 dribble 2PA'] + 8 * df['7+ dribble 2PA']) / ( df['0 dribble 2PA'] + df['1 dribble 2PA'] +  df['2 dribble 2PA'] + df['3-6 dribble 2PA'] + df['7+ dribble 2PA'])
df['touch_2pt_rtg'] = (1 * df['<2 sec 2PA'] + 4 * df['2-6 sec 2PA'] + 8 * df['6+ sec 2PA']) / (df['<2 sec 2PA'] + df['2-6 sec 2PA'] + df['6+ sec 2PA'])


rank_cols = ['early_2pa', 'avg_2pa', 'late_2pa', 'early_3pa', 'avg_3pa', 'late_3pa']
rank_col_names = ['rank_' + col for col in rank_cols]

for col in rank_cols:
    df['rank_' + col] = df[col] / df['MIN']

df.loc[df['MIN'] < 500, rank_col_names] = np.nan


for col in rank_col_names:
    #if col == 'rank_Fouls Committed Off.':
    #    df[col] = df[col].rank(pct=True, ascending=False)
    #else:
    df[col] = df[col].rank(pct=True)

df.loc[df['MIN'] < 500, ['open_3pt_rtg', 'dribble_2pt_rtg', 'touch_2pt_rtg']] = np.nan
df.loc[(df['0-2ft 3PA'] + df['2-4ft 3PA'] + df['4-6ft 3PA'] + df['6+ft 3PA']) < 50, ['open_3pt_rtg']] = np.nan
df.loc[(df['0 dribble 2PA'] + df['1 dribble 2PA'] +  df['2 dribble 2PA'] + df['3-6 dribble 2PA'] + df['7+ dribble 2PA']) < 50, ['dribble_2pt_rtg']] = np.nan
df.loc[(df['<2 sec 2PA'] + df['2-6 sec 2PA'] + df['6+ sec 2PA']) < 50, ['touch_2pt_rtg']] = np.nan

df['open_3pt_rtg'] = df['open_3pt_rtg'].rank(pct=True, ascending=False)
df['dribble_2pt_rtg'] = df['dribble_2pt_rtg'].rank(pct=True)
df['touch_2pt_rtg'] = df['touch_2pt_rtg'].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    ShotDifficultyStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        early_2pa = record['early_2pa'],
        average_2pa = record['avg_2pa'],
        late_2pa = record['late_2pa'],
        early_3pa = record['early_3pa'],
        average_3pa = record['avg_3pa'],
        late_3pa = record['late_3pa'],
        rank_per_min_early_2pa = 100.0 * record['rank_early_2pa'],
        rank_per_min_early_3pa = 100.0 * record['rank_early_3pa'],
        rank_per_min_avg_2pa = 100.0 * record['rank_avg_2pa'],
        rank_per_min_avg_3pa = 100.0 * record['rank_avg_3pa'],
        rank_per_min_late_2pa = 100.0 * record['rank_late_2pa'],
        rank_per_min_late_3pa = 100.0 * record['rank_late_3pa'],
        rank_open_3pa = 100.0 * record['open_3pt_rtg'],
        rank_touch_2pa = 100.0 * record['touch_2pt_rtg'],
        rank_dribble_2pa = 100.0 * record['dribble_2pt_rtg']
    ) for record in records
]
ShotDifficultyStat.objects.bulk_create(model_instances)
