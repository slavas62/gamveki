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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='\u0434\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f (UTC) \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u043e MODIS')),
                ('confidence', models.IntegerField(verbose_name='\u0434\u043e\u0441\u0442\u043e\u0432\u0435\u0440\u043d\u043e\u0441\u0442\u044c (0-100%)')),
                ('frp', models.FloatField(verbose_name='\u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u043f\u043e\u0436\u0430\u0440\u0430')),
                ('brightness21', models.FloatField(verbose_name='\u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043e \u043a\u0430\u043d\u0430\u043b\u0443 21/22 (\u0432 \u041a\u0435\u043b\u044c\u0432\u0438\u043d\u0430\u0445)')),
                ('brightness31', models.FloatField(verbose_name='\u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043f\u043e \u043a\u0430\u043d\u0430\u043b\u0443 31 (\u0432 \u041a\u0435\u043b\u044c\u0432\u0438\u043d\u0430\u0445)')),
                ('scan', models.FloatField(verbose_name='\u0440\u0430\u0437\u043c\u0435\u0440 \u043f\u0438\u043a\u0441\u0435\u043b\u0430 \u0432 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('track', models.FloatField(verbose_name='\u0440\u0430\u0437\u043c\u0435\u0440 \u043f\u0438\u043a\u0441\u0435\u043b\u0430 \u0432 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u0442\u0440\u0430\u0435\u043a\u0442\u043e\u0440\u0438\u0438')),
                ('version', models.CharField(max_length=10, verbose_name='\u0432\u0435\u0440\u0441\u0438\u044f')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'MODIS \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0436\u0430\u0440\u0435',
                'verbose_name_plural': 'MODIS \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u043e\u0436\u0430\u0440\u0430\u0445',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sattelite', models.CharField(unique=True, max_length=5, choices=[('Aqua', 'Aqua'), ('Terra', 'Terra')])),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0443\u0442\u043d\u0438\u043a',
                'verbose_name_plural': '\u0421\u043f\u0443\u0442\u043d\u0438\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='firms',
            name='satellite',
            field=models.ForeignKey(to='fires_app.Satellite'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='firms',
            unique_together=set([('geom', 'date')]),
        ),
    ]
