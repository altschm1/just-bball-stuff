# Generated by Django 3.2.7 on 2022-09-07 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BallHandlingStat',
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
                ('touches', models.IntegerField(default=0)),
                ('backcourt_touches', models.IntegerField(default=0)),
                ('frontcourt_touches', models.IntegerField(default=0)),
                ('elbow_touches', models.IntegerField(default=0)),
                ('post_ups', models.IntegerField(default=0)),
                ('paint_touches', models.IntegerField(default=0)),
                ('drives', models.IntegerField(default=0)),
                ('dribbles', models.IntegerField(default=0)),
                ('time_of_poss', models.IntegerField(default=0)),
                ('lost_balls', models.IntegerField(default=0)),
                ('rank_per_min_touches', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_backcourt_touches', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_frontcourt_touches', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_elbow_touches', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_post_ups', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_paint_touches', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_drives', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_dribbles', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_time_of_poss', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_lost_balls', models.FloatField(default=0.0, null=True)),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
