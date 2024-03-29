# Generated by Django 3.2.7 on 2021-09-21 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RimProtectionStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=120)),
                ('season', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=3)),
                ('age', models.IntegerField(default=0)),
                ('height_in', models.IntegerField(default=0)),
                ('weight_lb', models.IntegerField(default=0)),
                ('games_played', models.IntegerField(default=0)),
                ('minutes_played', models.IntegerField(default=0)),
                ('isolation_poss', models.IntegerField(default=0)),
                ('isolation_pts', models.IntegerField(default=0)),
                ('isolation_percentile', models.FloatField(default=0.0)),
                ('isolation_ppp', models.FloatField(default=0.0)),
                ('isolation_freq', models.FloatField(default=0.0)),
                ('ball_handler_poss', models.IntegerField(default=0)),
                ('ball_handler_pts', models.IntegerField(default=0)),
                ('ball_handler_percentile', models.FloatField(default=0.0)),
                ('ball_handler_ppp', models.FloatField(default=0.0)),
                ('ball_handler_freq', models.FloatField(default=0.0)),
                ('roll_man_poss', models.IntegerField(default=0)),
                ('roll_man_pts', models.IntegerField(default=0)),
                ('roll_man_percentile', models.FloatField(default=0.0)),
                ('roll_man_ppp', models.FloatField(default=0.0)),
                ('roll_man_freq', models.FloatField(default=0.0)),
                ('post_up_poss', models.IntegerField(default=0)),
                ('post_up_pts', models.IntegerField(default=0)),
                ('post_up_percentile', models.FloatField(default=0.0)),
                ('post_up_ppp', models.FloatField(default=0.0)),
                ('post_up_freq', models.FloatField(default=0.0)),
                ('hand_off_poss', models.IntegerField(default=0)),
                ('hand_off_pts', models.IntegerField(default=0)),
                ('hand_off_percentile', models.FloatField(default=0.0)),
                ('hand_off_ppp', models.FloatField(default=0.0)),
                ('hand_off_freq', models.FloatField(default=0.0)),
                ('off_screen_poss', models.IntegerField(default=0)),
                ('off_screen_pts', models.IntegerField(default=0)),
                ('off_screen_percentile', models.FloatField(default=0.0)),
                ('off_screen_ppp', models.FloatField(default=0.0)),
                ('off_screen_freq', models.FloatField(default=0.0)),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
