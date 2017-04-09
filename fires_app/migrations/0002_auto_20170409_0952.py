# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fires_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fire',
            name='version',
            field=models.CharField(max_length=6, verbose_name='\u0432\u0435\u0440\u0441\u0438\u044f'),
            preserve_default=True,
        ),
    ]
