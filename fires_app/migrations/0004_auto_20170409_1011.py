# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fires_app', '0003_auto_20170409_1005'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fire',
            unique_together=set([('geometry', 'date')]),
        ),
    ]
