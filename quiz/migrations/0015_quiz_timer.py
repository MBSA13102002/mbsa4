# Generated by Django 3.1.2 on 2020-10-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20201023_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timer',
            field=models.SmallIntegerField(default=60),
        ),
    ]
