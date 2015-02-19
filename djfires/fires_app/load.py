import os
from django.contrib.gis.utils import LayerMapping
from fires_app.models import Firms, firms_mapping

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))
shp = '/home/alexander/Загрузки/FIRMS/2014-07-01-00/World_7d.shp'

def run(verbose=True):
    lm = LayerMapping(Firms, shp, firms_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
