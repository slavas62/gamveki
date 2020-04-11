# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fires_app', '0004_siteconfiguration_url_viirs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='url_viirs',
            field=models.URLField(default=b'https://firms.modaps.eosdis.nasa.gov/active_fire/viirs/shapes/zips/VNP14IMGTDL_NRT_Global_24h.zip', verbose_name='URL VIIRS'),
        ),
    ]
