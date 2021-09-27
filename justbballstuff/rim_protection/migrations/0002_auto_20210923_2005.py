# Generated by Django 3.2.7 on 2021-09-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rim_protection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved',
        ),
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved_per_game',
        ),
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved_per_game_score',
        ),
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved_per_min',
        ),
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved_per_min_score',
        ),
        migrations.RemoveField(
            model_name='rimprotectionstat',
            name='points_saved_score',
        ),
        migrations.AddField(
            model_name='rimprotectionstat',
            name='diff_fg_pct',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='rimprotectionstat',
            name='diff_fg_pct_score',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]