# -*- coding: utf-8 -*-
import urllib2
import zipfile
import tempfile
import os
from django.contrib.gis.gdal import DataSource
from datetime import datetime
from decimal import Decimal
from fires_app.models import Fire, Satellite

class Loader():
    def __init__(self, url):
        self.url = url
        
    def download(self):
        tmp_zip_shape = open('/home/alexander/proj/fires_downloader/fires_downloader/Global_24h.zip', 'wb')
        tmp_zip_shape.write(urllib2.urlopen(self.url).read())
        return tmp_zip_shape

class Importer():
    
    def __init__(self, model, url):
        self.model = model
        self.url = url
        self.loader = Loader(url)
    
    def load_to_db(self):
    #1 Unzip and Open ds
        zip_file = zipfile.ZipFile(self.loader.download().name)
        zdir = '/home/alexander/proj/fires_downloader/fires_downloader/unzip2'
        for name in zip_file.namelist():
            data = zip_file.read(name)
            outfile = os.path.join(zdir, name)
            f = open(outfile, 'wb')
            f.write(data)
        f.close() 
        zip_file.close()
        self.ds = DataSource('/home/alexander/proj/fires_downloader/fires_downloader/unzip2/Global_24h.shp')
        self.layer = self.ds[0]
        for feature in self.layer:
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
