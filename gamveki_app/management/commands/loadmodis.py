from django.core.management.base import BaseCommand, CommandError
from fires_app.loader import ModisDBLoader
from fires_app.models import SiteConfiguration

class Command(BaseCommand):
    help = 'Update MODIS'

    def handle(self, *args, **options):
        try:
            ModisDBLoader().update(SiteConfiguration.get_solo().url_modis)
        except Exception as e:
            raise CommandError('MODIS update error. %s', e)
