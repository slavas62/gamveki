# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from solo.models import SingletonModel


class Satellite(models.Model):
    satellite = models.CharField(u'спутник', max_length=5, unique=True)
    short_satellite_name = models.CharField(u'спутник сокращенно', max_length=1, unique=True)

    class Meta:
        verbose_name = u'Спутник'
        verbose_name_plural = u'Спутники'
        db_table = 'satellite'
    
    def __str__(self):
        return str(self.satellite)
 

class FireModis(models.Model):
#    date = models.DateTimeField(u'дата и время (UTC) получения данных о MODIS')
    date = models.DateField(u'дата получения данных о MODIS', null=True)
    time = models.TimeField(u'дата и время (UTC) получения данных о MODIS', null=True)
    satellite = models.ForeignKey(Satellite)
    confidence = models.DecimalField(u'достоверность (0-100%)', max_digits=3, decimal_places=0)
    frp = models.DecimalField(u'мощность пожара', max_digits=5, decimal_places=1)
    brightness21 = models.DecimalField(u'температура по каналу 21/22 (в Кельвинах)', max_digits=4, decimal_places=1)
    brightness31 = models.DecimalField(u'температура по каналу 31 (в Кельвинах)', max_digits=4, decimal_places=1)
    scan = models.DecimalField(u'размер пиксела в направлении сканирования', max_digits=2, decimal_places=1)
    track = models.DecimalField(u'размер пиксела в направлении траектории', max_digits=2, decimal_places=1)
    version = models.CharField(u'версия', max_length=6)
    night = models.BooleanField(u'Признак ночного снимка', default=0)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta:
        unique_together = ('geometry', 'date')
        verbose_name = u'MODIS данные о пожаре'
        verbose_name_plural = u'MODIS данные о пожарах'
        db_table = 'fireModis'
    
    def __str__(self):
        return str(self.date)

class FireViirs(models.Model):
#    date = models.DateTimeField(u'дата и время (UTC) получения данных о VIIRS')
    date = models.DateField(u'дата получения данных о VIIRS', null=True)
    time = models.TimeField(u'время (UTC) получения данных о VIIRS', null=True)
    satellite = models.ForeignKey(Satellite)
    confidence = models.DecimalField(u'достоверность (0-100%)', max_digits=3, decimal_places=0)
    frp = models.DecimalField(u'мощность пожара', max_digits=5, decimal_places=1)
    brightness_ti4 = models.DecimalField(u'температура по каналу I-4 (в Кельвинах)', max_digits=4, decimal_places=1)
    brightness_ti5 = models.DecimalField(u'температура по каналу I-5 (в Кельвинах)', max_digits=4, decimal_places=1)
    scan = models.DecimalField(u'размер пиксела в направлении сканирования', max_digits=2, decimal_places=1)
    track = models.DecimalField(u'размер пиксела в направлении траектории', max_digits=2, decimal_places=1)
    version = models.CharField(u'версия', max_length=6)
    night = models.BooleanField(u'Признак ночного снимка', default=0)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta:
        unique_together = ('geometry', 'date')
        verbose_name = u'VIIRS данные о пожаре'
        verbose_name_plural = u'VIIRS данные о пожарах'
        db_table = 'fireViirs'
    
    def __str__(self):
        return str(self.date)
    

class SiteConfiguration(SingletonModel):
    url_modis = models.URLField(u'URL MODIS', default='https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_Global_24h.zip')
    url_viirs = models.URLField(u'URL VIIRS', default='https://firms.modaps.eosdis.nasa.gov/active_fire/viirs/shapes/zips/VNP14IMGTDL_NRT_Global_24h.zip')

    def __unicode__(self):
        return u'Настройки сайта'

    class Meta:
        verbose_name = 'Настройки сайта'