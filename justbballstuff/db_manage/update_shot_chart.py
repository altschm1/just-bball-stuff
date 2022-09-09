# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from shot_chart.models import ShotChartStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
ShotChartStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/shot-locations/final_data/{season_param}/final.csv')

cols = ['FTM','FTA','RA FGM','RA FGA','non-RA Paint FGA','non-RA Paint FGM','Midrange FGM','Midrange FGA','Corner FGM','Corner FGA','ATB FGM','ATB FGA']
df[cols] = df[cols].replace('-', 0)
df[cols] = df[cols].astype(int)


df['ft%'] = 100.0 * df['FTM'] / df['FTA']
df['rim%'] = 100.0 * df['RA FGM'] / df['RA FGA']
df['floater%'] = 100.0 *  df['non-RA Paint FGM'] / df['non-RA Paint FGA']
df['mid%'] = 100.0 * df['Midrange FGM'] / df['Midrange FGA']
df['corner%'] = 100.0 * df['Corner FGM'] / df['Corner FGA']
df['atb%'] = 100.0 * df['ATB FGM'] / df['ATB FGA']


rank_cols = ['FTA', 'RA FGA', 'non-RA Paint FGA', 'Midrange FGA', 'Corner FGA', 'ATB FGA']
rank_perc_cols = ['ft%', 'rim%', 'floater%', 'mid%', 'corner%', 'atb%']
rank_col_names = ['rank_' + col for col in rank_cols]

for col in rank_cols:
    df['rank_' + col] = df[col] / df['MIN']

df.loc[df['MIN'] < 500, rank_col_names] = np.nan

for col in rank_col_names:
    df[col] = df[col].rank(pct=True)

for perc_col, col in zip(rank_perc_cols, rank_cols):
    df['rank_' + perc_col] = df[perc_col]
    df.loc[df[col] < 50, ['rank_' + perc_col]] = np.nan
    df['rank_' + perc_col] = df['rank_' + perc_col].rank(pct=True)

print(df)

records = df.to_dict('records')
model_instances = [
    ShotChartStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        fta = record['FTA'],
        rim_fga = record['RA FGA'],
        floater_fga = record['non-RA Paint FGA'],
        midrange_fga = record['Midrange FGA'],
        corner_fga = record['Corner FGA'],
        atb_fga = record['ATB FGA'],
        ft_perc = record['ft%'],
        rim_perc = record['rim%'],
        floater_perc = record['floater%'],
        midrange_perc = record['mid%'],
        corner_perc = record['corner%'],
        atb_perc = record['atb%'],
        rank_per_min_fta = 100.0 * record['rank_FTA'],
        rank_per_min_rim_fga = 100.0 * record['rank_RA FGA'],
        rank_per_min_floater_fga = 100.0 * record['rank_non-RA Paint FGA'],
        rank_per_min_midrange_fga = 100.0 * record['rank_Midrange FGA'],
        rank_per_min_corner_fga = 100.0 * record['rank_Corner FGA'],
        rank_per_min_atb_fga = 100.0 * record['rank_ATB FGA'],
        rank_ft_perc = 100.0 * record['rank_ft%'],
        rank_rim_perc = 100.0 * record['rank_rim%'],
        rank_floater_perc = 100.0 * record['rank_floater%'],
        rank_midrange_perc = 100.0 * record['rank_mid%'],
        rank_corner_perc = 100.0 * record['rank_corner%'],
        rank_atb_perc = 100.0 * record['rank_atb%']
    ) for record in records
]
ShotChartStat.objects.bulk_create(model_instances)
