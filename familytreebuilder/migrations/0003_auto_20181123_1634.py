# Generated by Django 2.1.3 on 2018-11-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytreebuilder', '0002_auto_20181123_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='photo_path',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='photo_path',
            new_name='photo',
        ),
    ]