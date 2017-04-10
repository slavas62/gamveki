import logging

from celery import shared_task
from fires_app.loader import DBLoader

logger = logging.getLogger('update.main_updater')


@shared_task
def fire_update_task():
    try:
        return DBLoader().update('https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_Global_24h.zip')
    except Exception as e:
        logger.error('%s updater error: %s' % (DBLoader, e))