import os.path

# Get the project root path
from django.conf import settings

# Image file path and name, set it to be at project root by default
IMAGES_FILE = settings.BASE_DIR + os.path.sep + 'images.txt'
IMAGES_PATH = settings.BASE_DIR + os.path.sep + 'saved_images' + os.path.sep
