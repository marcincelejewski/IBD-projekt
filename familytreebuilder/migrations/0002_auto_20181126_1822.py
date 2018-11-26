# Generated by Django 2.1.3 on 2018-11-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familytreebuilder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='family',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
