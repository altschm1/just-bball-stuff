# Generated by Django 3.2.7 on 2022-09-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShotChartStat',
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
                ('fta', models.IntegerField(default=0)),
                ('rim_fga', models.IntegerField(default=0)),
                ('floater_fga', models.IntegerField(default=0)),
                ('midrange_fga', models.IntegerField(default=0)),
                ('corner_fga', models.IntegerField(default=0)),
                ('atb_fga', models.IntegerField(default=0)),
                ('ft_perc', models.FloatField(default=0.0, null=True)),
                ('rim_perc', models.FloatField(default=0.0, null=True)),
                ('floater_perc', models.FloatField(default=0.0, null=True)),
                ('midrange_perc', models.FloatField(default=0.0, null=True)),
                ('corner_perc', models.FloatField(default=0.0, null=True)),
                ('atb_perc', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_fta', models.IntegerField(default=0)),
                ('rank_per_min_rim_fga', models.IntegerField(default=0)),
                ('rank_per_min_floater_fga', models.IntegerField(default=0)),
                ('rank_per_min_midrange_fga', models.IntegerField(default=0)),
                ('rank_per_min_corner_fga', models.IntegerField(default=0)),
                ('rank_per_min_atb_fga', models.IntegerField(default=0)),
                ('rank_ft_perc', models.FloatField(default=0.0, null=True)),
                ('rank_rim_perc', models.FloatField(default=0.0, null=True)),
                ('rank_floater_perc', models.FloatField(default=0.0, null=True)),
                ('rank_midrange_perc', models.FloatField(default=0.0, null=True)),
                ('rank_corner_perc', models.FloatField(default=0.0, null=True)),
                ('rank_atb_perc', models.FloatField(default=0.0, null=True)),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
