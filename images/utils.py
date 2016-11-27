import requests
import shutil
import os
import datetime

from images.models import Image
from images import settings as image_settings


def save_latest_images(image_file=None, image_path=None):
    """
    Processes the file with images URLs and saves them into db
    :param image_file: The file containing image urls, if empty it defaults to the one in settings
    :param image_path: The place to store images, if empty it defaults to the one in settings
    """
    from images.tasks import logger
    images_file = image_file if image_file else image_settings.IMAGES_FILE
    saved_images_path = image_path if image_path else image_settings.IMAGES_PATH
    # Check if file is present, skip otherwise
    if os.path.isfile(images_file):
        # Open images file and process each line
        file = open(images_file, 'r')
        for image in file:
            image = image.rstrip('\n')
            response = requests.get(image, stream=True)
            # Get file name
            image_name = os.path.basename(image)
            try:
                with open(saved_images_path + image_name, 'xb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                # Save object in bd if does not exist
                if not Image.objects.filter(image_url=image).exists():
                    image = Image(
                        title=image_name,
                        image_url=image,
                        location=saved_images_path + image_name,
                        created_on=datetime.datetime.utcnow(),
                    )
                    image.save()
                    logger.info('Saved image {0} correctly to db and to disk'.format(image_name))
                del response
            except IOError:
                logger.error('An error occured trying to save image to disk for image {0}'.format(image_name))
                continue
    else:
        logger.error('Could not find file {0} with images urls'.format(images_file))