# Generated by Django 3.2.23 on 2023-12-15 12:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_at',
                    models.DateTimeField(default=django.utils.timezone.localtime),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team_1_score', models.IntegerField()),
                ('team_2_score', models.IntegerField()),
                (
                    'team_1',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='home_games',
                        to='teams.team',
                    ),
                ),
                (
                    'team_2',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='away_games',
                        to='teams.team',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
