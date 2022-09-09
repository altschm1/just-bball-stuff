# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from passing.models import PassingStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
PassingStat.objects.filter(season=season_param).delete()


# update Player model
df = pd.read_csv(f'C:/Users/18562/passing/final_data/{season_param}/final.csv')
df['adjusted_ast'] = df['ASTAdj'] - df['SecondaryAST']

df['rank_passes'] = df['PassesMade'] / df['MIN']
df['rank_adj_ast'] = df['adjusted_ast'] / df['MIN']
df['rank_hockey_ast'] = df['SecondaryAST'] / df['MIN']
df['rank_potential_ast'] = df['PotentialAST'] / df['MIN']
df['rank_bad_passes'] = df['Turnovers BadPass'] / df['MIN']

df.loc[df['MIN'] < 500, ['rank_passes', 'rank_adj_ast', 'rank_hockey_ast', 'rank_potential_ast', 'rank_bad_passes']] = np.nan


df['rank_passes'] = df['rank_passes'].rank(pct=True)
df['rank_adj_ast'] = df['rank_adj_ast'].rank(pct=True)
df['rank_hockey_ast'] = df['rank_hockey_ast'].rank(pct=True)
df['rank_potential_ast'] = df['rank_potential_ast'].rank(pct=True)
df['rank_bad_passes'] = df['rank_bad_passes'].rank(pct=True, ascending=False)

print(df)

records = df.to_dict('records')
model_instances = [
    PassingStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        passes = record['PassesMade'],
        adj_assists = record['adjusted_ast'],
        hockey_assists = record['SecondaryAST'],
        potential_assists = record['PotentialAST'],
        bad_passes = record['Turnovers BadPass'],
        rank_per_min_passes = 100.0 * record['rank_passes'],
        rank_per_min_adj_assists = 100.0 * record['rank_adj_ast'],
        rank_per_min_hockey_assists = 100.0 * record['rank_hockey_ast'],
        rank_per_min_potential_assists = 100.0 * record['rank_potential_ast'],
        rank_per_min_bad_passes = 100.0 * record['rank_bad_passes']
    ) for record in records
]
PassingStat.objects.bulk_create(model_instances)
