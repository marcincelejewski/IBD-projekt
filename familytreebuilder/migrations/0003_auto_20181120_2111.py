# Generated by Django 2.1.3 on 2018-11-20 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('familytreebuilder', '0002_auto_20181120_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 20, 20, 11, 11, 874618, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=40, verbose_name='Hasło'),
        ),
    ]
