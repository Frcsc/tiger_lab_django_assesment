# Generated by Django 3.2.23 on 2023-12-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='type_of_user',
            field=models.CharField(
                choices=[
                    ('basic_users', 'Basic Users'),
                    ('admin_users', 'Admin Usesrs'),
                ],
                default='basic_users',
                max_length=128,
            ),
        ),
    ]
