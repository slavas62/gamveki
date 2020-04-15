from django.db import transaction
from datetime import datetime
from decimal import Decimal
from fires_app.models import FireModis, FireViirs, Satellite
from django.contrib.gis.gdal import DataSource, OGRGeometry
from django.contrib.gis.geos import GEOSGeometry
import logging
import random

class DBLoader(object):
    
    LOGGER_NAME = 'update.abstract.dbloader'
    
    def __init__(self):
        self.logger = logging.getLogger(self.LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
    
    def fire_from_feature(self, feature):
        raise NotImplementedError
    
    @transaction.atomic
    def update_features(self, features, filter_geometry=None):
        self.logger.info('Update feature...')
        for feat in features:
            if feat.geom.geom_type != 'Point':
                self.logger.warning('Invalid geometry type: %s' % feat.geom.wkt)
                continue
            try:
#                fire, created = self.fire_from_feature(feat)
                self.fire_from_feature(feat)
            except TypeError as e:
                self.logger.warning('Data error: %s' % str(e))
                continue
            except ValueError as e:
                self.logger.warning('Value error: %s' % str(e))
                continue
            if (filter_geometry and not fire.geometry.intersects(filter_geometry)):
                continue
#            if not created:
#                continue
            
#            fire.save()
        self.logger.info('Update feature done.')
    
    def update(self, url, filter_geometry=None):
        if filter_geometry:
            if isinstance(filter_geometry, str):
                filter_geometry = GEOSGeometry(filter_geometry)
            elif isinstance(filter_geometry, OGRGeometry):
                filter_geometry = filter_geometry.geos
            else:
                raise TypeError('invalid filter_geometry type')
            
        self.logger.info('Start downloading...')
        try:
            ds = DataSource(''.join(['/vsizip//vsicurl/', url]))
            self.logger.info('Download done: %s' % (''.join(['/vsizip//vsicurl/', url])))
        except Exception as e:
            self.logger.error('Downloading failed %s. %s' % (url, str(e)))
            return
        layer = ds[0]
        self.update_features(layer, filter_geometry)
    

class ModisDBLoader(DBLoader):
    
    LOGGER_NAME = 'update.modis.dbloader'
    
    def __init__(self):
        self.logger = logging.getLogger(self.LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
    
    def fire_from_feature(self, feature):
        acq_datetime = ''.join([str(feature['ACQ_DATE']), str(feature['ACQ_TIME'])])
        data = {
            'date': datetime.strptime(acq_datetime, '%Y-%m-%d%H%M'),
            'satellite': Satellite.objects.get(short_satellite_name=str(feature['SATELLITE'])),
            'confidence': Decimal(str(feature['CONFIDENCE'])),
            'frp': Decimal(str(feature['FRP'])),
            'brightness21': Decimal(str(feature['BRIGHTNESS'])),
            'brightness31': Decimal(str(feature['BRIGHT_T31'])),
            'scan': Decimal(str(feature['SCAN'])),
            'track': Decimal(str(feature['TRACK'])),
            'version': str(feature['VERSION']),
            'night': bool(True if feature['DAYNIGHT']=='N' else False),
            'geometry': feature.geom.geos
        }
        
        try:
            fire = FireModis.objects.get(geometry=data['geometry'], date=data['date'])
            if fire.confidence < data['confidence']:
                fire.update(**data)
                fire.save()
                self.logger.info('Update exist record with small confidence.Id %s confidence %s'%(fire.id, data['confidence']))
                return fire, True
        except FireModis.DoesNotExist:
            pass

            self.logger.info('Add fire Modis: %s %s' % (fire.id, data['date']))
            return FireModis.objects.get_or_create(**data)
#            try: 
#                self.logger.info('Add fire Modis: %s %s' % (fire.id, data['date']))
#                return FireModis.objects.get_or_create(**data)
#            except DatabaseError as e:
#                self.logger.error('%s database error: %s' % (FireModis, e))
#                return fire, False


class ViirsDBLoader(DBLoader):
    
    LOGGER_NAME = 'update.viirs.dbloader'
    
    def __init__(self):
        self.logger = logging.getLogger(self.LOGGER_NAME)
        self.logger.setLevel(logging.INFO)
        
    def get_confidence(self, confidence):
        if confidence == 'low':
            return 0
        if confidence == 'nominal':
            return 50
        if confidence == 'high':
            return 100
    
    def fire_from_feature(self, feature):
        acq_datetime = ''.join([str(feature['ACQ_DATE']), str(feature['ACQ_TIME'])])
        data = {
            'date': datetime.strptime(acq_datetime, '%Y-%m-%d%H%M'),
            'satellite': Satellite.objects.get(short_satellite_name=str(feature['SATELLITE'])),
            'confidence': self.get_confidence(str(feature['CONFIDENCE'])),
            'frp': Decimal(str(feature['FRP'])),
            'brightness_ti4': Decimal(str(feature['BRIGHT_TI4'])),
            'brightness_ti5': Decimal(str(feature['BRIGHT_TI5'])),
            'scan': Decimal(str(feature['SCAN'])),
            'track': Decimal(str(feature['TRACK'])),
            'version': str(feature['VERSION']),
            'night': bool(True if feature['DAYNIGHT']=='N' else False),
            'geometry': feature.geom.geos
        }
        try:
            fire = FireViirs.objects.get(geometry=data['geometry'], date=data['date'])
            if fire.confidence < data['confidence']:
                fire.update(**data)
                fire.save()
                self.logger.info('Update exist record with small confidence.Id %s confidence %s'%(fire.id, data['confidence']))
                return fire, True
        except FireViirs.DoesNotExist:
            
            try: 
                self.logger.info('Add fire Viirs: %s %s' % (fire.id, data['date']))
                return FireViirs.objects.get_or_create(**data)
            except DatabaseError as e:
                self.logger.error('%s database error: %s' % (FireViirs, e))
                return fire, False
