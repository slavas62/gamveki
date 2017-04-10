import logging
from celery import shared_task
from fires_app.loader import DBLoader
from fires_app.models import SiteConfiguration

logger = logging.getLogger('update.main_updater')


@shared_task
def fire_update_task():
    try:
        return DBLoader().update(SiteConfiguration.get_solo().url_modis)
    except Exception as e:
        logger.error('%s updater error: %s' % (DBLoader, e))