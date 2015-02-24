from django.contrib.gis.utils import LayerMapping
from fires_app.models import Firms

class Loader():
    def __init__(self, url, path):
        self.url = url
        self.path = path
        
    def do_download(self):
        return '/home/alexander/Загрузки/FIRMS/2014-07-01-04/World_24h.shp'

class Importer():
    def __init__(self, model, data):
        self.model = model
        self.data = data
    def do_import(self):
    #1 Open ds

    #2 Iterate thought ds

    #3 Save features skip same features add logic where same points but different confidence
        pass    
    


if __name__ == '__main__':
    pass
    # download
    url = ''
    path = ''
    loader = Loader(url, path)
    shp = loader.do_download()
    # import to db
    imp = Importer(Firms, shp)
    imp.do_import()
