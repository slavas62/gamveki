from django.core.management.base import BaseCommand, CommandError
from fires_app.loader import DBLoader
from fires_app.models import SiteConfiguration

class Command(BaseCommand):
    help = 'Update MODIS'

    def handle(self, *args, **options):
        try:
            DBLoader().update(SiteConfiguration.get_solo().url_modis)
        except Exception as e:
            raise CommandError('Update error. %s', e)
