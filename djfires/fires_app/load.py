# -*- coding: utf-8 -*-
from django.contrib.gis.gdal import DataSource
from datetime import datetime
from decimal import Decimal
from fires_app.models import Fire, Satellite
import logging

# create and set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# file handler
fh = logging.FileHandler('load_logging.log')
fh.setLevel(logging.DEBUG)
# formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

class Importer():
    
    def __init__(self, model, url):
        self.model = model
        self.url = url
    
    def load_to_db(self):
        ds_path = ''.join(['/vsizip/vsicurl/', self.url])
        logger.info('Start downloading...')
        try:
            ds = DataSource(ds_path)
        except:
            logger.warning('Downloading failed!')
            return
        logger.info('Downloading complete!')    
        layer = ds[0]
        number_saved_features = 0
        number_unsaved_features = 0
        logger.info('Start importing...')
        for feature in layer:
            try:
                m = self.feature_to_model(feature)
                m.save()
                number_saved_features += 1
            except:
                number_unsaved_features += 1
        long_string = 'Import complete. Number saved features {}. Number unsaved features {}.'
        logger.info(long_string.format(number_saved_features, number_unsaved_features))
    
    def feature_to_model(self, feature):
        acq_datetime = ''.join([str(feature['ACQ_DATE']), 
                                str(feature['ACQ_TIME'])])
        dt = datetime.strptime(acq_datetime, '%Y-%m-%d%H%M')
        data = {
            'date': dt,
            'satellite': Satellite.objects.get(short_satellite_name=str(feature['SATELLITE'])),
            'confidence': Decimal(str(feature['CONFIDENCE'])),
            'frp': Decimal(str(feature['FRP'])),
            'brightness21': Decimal(str(feature['BRIGHTNESS'])),
            'brightness31': Decimal(str(feature['BRIGHT_T31'])),
            'scan': Decimal(str(feature['SCAN'])),
            'track': Decimal(str(feature['TRACK'])),
            'version': Decimal(str(feature['VERSION'])),
            'geometry': feature.geom.geos
        }
        return Fire(**data)
