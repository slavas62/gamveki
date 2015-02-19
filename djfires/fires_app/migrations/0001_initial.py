# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('brightness', models.FloatField()),
                ('scan', models.FloatField()),
                ('track', models.FloatField()),
                ('acq_date', models.DateField()),
                ('acq_time', models.CharField(max_length=5)),
                ('satellite', models.CharField(max_length=1)),
                ('confidence', models.IntegerField()),
                ('version', models.CharField(max_length=10)),
                ('bright_t31', models.FloatField()),
                ('frp', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
