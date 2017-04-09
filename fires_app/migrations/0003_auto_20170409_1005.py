# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fires_app', '0002_auto_20170409_0952'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fire',
            unique_together=set([('geometry', 'date', 'confidence')]),
        ),
    ]
