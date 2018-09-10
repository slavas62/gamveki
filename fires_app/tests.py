#from django.db import transaction
from datetime import datetime
from decimal import Decimal
#from fires_app.models import FireModis, FireViirs, Satellite
#from django.contrib.gis.gdal import DataSource, OGRGeometry
#from django.contrib.gis.geos import GEOSGeometry


# Create your tests here.
def main():
    acq_datetime = ''.join(['2018-09-06', '0000'])
#    fire = FireModis.objects.get(geometry=data['geometry'], date=data['date'])
    print (acq_datetime)
    print (datetime.strptime(acq_datetime, '%Y-%m-%d%H%M'))

main()