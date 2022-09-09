# Generated by Django 3.2.7 on 2022-09-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayTypeStat',
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
                ('transition_poss', models.IntegerField(default=0)),
                ('on_ball_screen_poss', models.IntegerField(default=0)),
                ('one_on_one_poss', models.IntegerField(default=0)),
                ('off_ball_poss', models.IntegerField(default=0)),
                ('roll_poss', models.IntegerField(default=0)),
                ('putback_poss', models.IntegerField(default=0)),
                ('rank_per_min_transition_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_on_ball_screen_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_one_on_one_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_off_ball_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_roll_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_putback_poss', models.FloatField(default=0.0, null=True)),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
