from django.contrib.gis.db import models

class Firms(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    brightness = models.FloatField()
    scan = models.FloatField()
    track = models.FloatField()
    acq_date = models.DateField()
    acq_time = models.CharField(max_length=5)
    satellite = models.CharField(max_length=1)
    confidence = models.IntegerField()
    version = models.CharField(max_length=10)
    bright_t31 = models.FloatField()
    frp = models.FloatField()
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for Firms model
firms_mapping = {
    'latitude' : 'LATITUDE',
    'longitude' : 'LONGITUDE',
    'brightness' : 'BRIGHTNESS',
    'scan' : 'SCAN',
    'track' : 'TRACK',
    'acq_date' : 'ACQ_DATE',
    'acq_time' : 'ACQ_TIME',
    'satellite' : 'SATELLITE',
    'confidence' : 'CONFIDENCE',
    'version' : 'VERSION',
    'bright_t31' : 'BRIGHT_T31',
    'frp' : 'FRP',
    'geom' : 'POINT',
}
