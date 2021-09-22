# move up one directory
import sys
sys.path.append('..')

# set environment for Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','justbballstuff.settings')
import django
django.setup()

from defense_synergy.models import DefensiveSynergyStat
import pandas as pd
import numpy as np

season_param = sys.argv[1]

# drop all the data for season_param
DefensiveSynergyStat.objects.filter(season=season_param).delete()

# update Player model
df = pd.read_csv(f'C:/Users/18562/synergy/final_data/{season_param}/defense.csv')

print(df)
records = df.to_dict('records')
model_instances = [
    DefensiveSynergyStat(
        player = record['Player'],
        season = season_param,
        team = record['Team'],
        age = record['Age'],
        height_in = record['Height'],
        weight_lb = record['Weight'],
        games_played = record['GP'],
        minutes_played = record['MIN'],
        isolation_poss = record['isolation_poss'],
        isolation_pts = record['isolation_pts'],
        isolation_ppp = record['isolation_ppp'],
        isolation_percentile = record['isolation_percentile'],
        isolation_freq = record['isolation_freq'],
        ball_handler_poss = record['ball-handler_poss'],
        ball_handler_pts = record['ball-handler_pts'],
        ball_handler_ppp = record['ball-handler_ppp'],
        ball_handler_percentile = record['ball-handler_percentile'],
        ball_handler_freq = record['ball-handler_freq'],
        roll_man_poss = record['roll-man_poss'],
        roll_man_pts = record['roll-man_pts'],
        roll_man_ppp = record['roll-man_ppp'],
        roll_man_percentile = record['roll-man_percentile'],
        roll_man_freq = record['roll-man_freq'],
        post_up_poss = record['playtype-post-up_poss'],
        post_up_pts = record['playtype-post-up_pts'],
        post_up_ppp = record['playtype-post-up_ppp'],
        post_up_percentile = record['playtype-post-up_percentile'],
        post_up_freq = record['playtype-post-up_freq'],
        spot_up_poss = record['spot-up_poss'],
        spot_up_pts = record['spot-up_pts'],
        spot_up_ppp = record['spot-up_ppp'],
        spot_up_percentile = record['spot-up_percentile'],
        spot_up_freq = record['spot-up_freq'],
        hand_off_poss = record['hand-off_poss'],
        hand_off_pts = record['hand-off_pts'],
        hand_off_ppp = record['hand-off_ppp'],
        hand_off_percentile = record['hand-off_percentile'],
        hand_off_freq = record['hand-off_freq'],
        off_screen_poss = record['off-screen_poss'],
        off_screen_pts = record['off-screen_pts'],
        off_screen_ppp = record['off-screen_ppp'],
        off_screen_percentile = record['off-screen_percentile'],
        off_screen_freq = record['off-screen_freq'],
    ) for record in records
]
DefensiveSynergyStat.objects.bulk_create(model_instances)
