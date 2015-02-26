# -*- coding: utf-8 -*-
from django.contrib.gis.gdal import DataSource
from datetime import datetime
from decimal import Decimal
from fires_app.models import Fire, Satellite


class Importer():
    
    def __init__(self, model, url):
        self.model = model
        self.url = url
    
    def load_to_db(self):
    #1 Open remote ds
        ds_path = ''.join(['/vsizip/vsicurl/', self.url])
        ds = DataSource(ds_path)
        layer = ds[0]
        for feature in layer:
            try:
                m = self.feature_to_model(feature)
                m.save()
            except:
                pass
    
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
