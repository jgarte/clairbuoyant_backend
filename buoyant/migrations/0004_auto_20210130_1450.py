# Generated by Django 3.1.3 on 2021-01-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buoyant', '0003_auto_20210119_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meteorological',
            name='air_temp',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='avg_wave_period',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='dewpoint_temp',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='dom_wave_period',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='sea_pressure',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='sea_temp',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='station_visibility',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='wave_height',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='wind_gust',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='meteorological',
            name='wind_speed',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]