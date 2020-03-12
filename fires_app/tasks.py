import logging
from celery import shared_task
from fires_app.loader import ModisDBLoader, ViirsDBLoader
from fires_app.models import SiteConfiguration

logger = logging.getLogger('update.main_updater')


@shared_task
def modis_update_task():
    print('------------ MODIS --------------')
    try:
        return ModisDBLoader().update(SiteConfiguration.get_solo().url_modis)
    except Exception as e:
        logger.error('%s updater error: %s' % (ModisDBLoader, e))

@shared_task
def viirs_update_task():
    print('------------ VIIRS --------------')
    try:
        return ViirsDBLoader().update(SiteConfiguration.get_solo().url_viirs)
    except Exception as e:
        logger.error('%s updater error: %s' % (ViirsDBLoader, e))