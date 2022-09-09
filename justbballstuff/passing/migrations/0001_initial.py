# Generated by Django 3.2.7 on 2022-09-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassingStat',
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
                ('passes', models.IntegerField(default=0)),
                ('adj_assists', models.IntegerField(default=0)),
                ('hockey_assists', models.IntegerField(default=0)),
                ('potential_assists', models.IntegerField(default=0)),
                ('bad_passes', models.IntegerField(default=0)),
                ('rank_per_min_passes', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_adj_assists', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_hockey_assists', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_potential_assists', models.FloatField(default=0.0, null=True)),
                ('rank_per_min_bad_passes', models.FloatField(default=0.0, null=True)),
            ],
            options={
                'unique_together': {('player', 'season')},
            },
        ),
    ]
