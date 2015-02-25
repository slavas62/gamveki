# -*- coding: utf-8 -*-
from django.contrib.gis.db import models


class Satellite(models.Model):
    SELECT_SATTELITE = (
                        (u'Aqua', u'Aqua'),
                        (u'Terra', u'Terra'),
                        )
    satellite = models.CharField(max_length=5, unique=True, choices=SELECT_SATTELITE)

    class Meta:
        verbose_name = u'Спутник'
        verbose_name_plural = u'Спутники'
        
    def __unicode__(self): # __unicode__ on Python 2
        return u'Спутник: %s' % (self.satellite)

class Firms(models.Model):
    date = models.DateTimeField(u'дата и время (UTC) получения данных о MODIS')
    satellite = models.ForeignKey(Satellite)
    confidence = models.DecimalField(u'достоверность (0-100%)', max_digits=3, decimal_places=0)
    frp = models.DecimalField(u'мощность пожара', max_digits=5, decimal_places=1)
    brightness21 = models.DecimalField(u'температура по каналу 21/22 (в Кельвинах)', max_digits=4, decimal_places=1)
    brightness31 = models.DecimalField(u'температура по каналу 31 (в Кельвинах)', max_digits=4, decimal_places=1)
    scan = models.DecimalField(u'размер пиксела в направлении сканирования', max_digits=2, decimal_places=1)
    track = models.DecimalField(u'размер пиксела в направлении траектории', max_digits=2, decimal_places=1)
    version = models.DecimalField(u'версия', max_digits=2, decimal_places=1)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta:
        unique_together = ('geom', 'date')
        verbose_name = u'MODIS данные о пожаре'
        verbose_name_plural = u'MODIS данные о пожарах'
        
    def __unicode__(self): # __unicode__ on Python 2
        return u'Дата: %s, Достоверность: %s' % (self.date, self.confidence)
        
    
    
# Auto-generated `LayerMapping` dictionary for Firms model
# firms_mapping = {
#     'latitude' : 'LATITUDE',
#     'longitude' : 'LONGITUDE',
#     'brightness' : 'BRIGHTNESS',
#     'scan' : 'SCAN',
#     'track' : 'TRACK',
#     'acq_date' : 'ACQ_DATE',
#     'acq_time' : 'ACQ_TIME',
#     'satellite' : 'SATELLITE',
#     'confidence' : 'CONFIDENCE',
#     'version' : 'VERSION',
#     'bright_t31' : 'BRIGHT_T31',
#     'frp' : 'FRP',
#     'geom' : 'POINT',
# }
