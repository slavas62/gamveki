from django.core.management.base import BaseCommand, CommandError
from fires_app.loader import ViirsDBLoader
from fires_app.models import SiteConfiguration

class Command(BaseCommand):
    help = 'Update VIIRS'

    def handle(self, *args, **options):
        try:
            ViirsDBLoader().update(SiteConfiguration.get_solo().url_viirs)
        except Exception as e:
            raise CommandError('VIIRS update error. %s', e)
