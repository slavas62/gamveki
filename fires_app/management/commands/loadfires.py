from django.core.management.base import BaseCommand
from fires_app.loader import DBLoader

class Command(BaseCommand):
    help = 'Update MODIS'

    def handle(self, *args, **options):
        DBLoader().update('https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_Global_24h.zip')

