from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from images.utils import save_latest_images

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="task_parse_images_file",
    ignore_result=True
)
def task_parse_images_file():
    """
    Parses images file and stores data in db
    """
    logger.info('Processing image files...')
    save_latest_images()
    logger.info('Processed image files!')