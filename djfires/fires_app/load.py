# -*- coding: utf-8 -*-
import urllib2
import zipfile
import tempfile


from django.contrib.gis.utils import LayerMapping
from fires_app.models import Firms

class Loader():
    def __init__(self, url):
        self.url = url
        
    def do_download(self):
        tmp_zip_shape = tempfile.SpooledTemporaryFile()
        tmp_zip_shape.write(urllib2.urlopen(self.url).read())
        return tmp_zip_shape

class Importer():
    def __init__(self, model, url):
        self.model = model
        self.url = url
        self.loader = Loader(url)
    def do_import(self):
    #1 Open ds

    #2 Iterate thought ds

    #3 Save features skip same features add logic where same points but different confidence
        pass    
