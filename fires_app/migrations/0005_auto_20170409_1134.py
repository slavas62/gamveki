# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fires_app', '0004_auto_20170409_1011'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='fire',
            table='fire',
        ),
        migrations.AlterModelTable(
            name='satellite',
            table='satellite',
        ),
    ]
