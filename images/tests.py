# -*- coding: utf-8 -*-
import os
import os.path
import shutil

from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.conf import settings

from images.models import Image
from images.utils import save_latest_images


class ImageFetcherTestCase(TestCase):

    def setUp(self):
        # Override the client with the API client
        # See: http://www.django-rest-framework.org/api-guide/testing/
        self.factory = RequestFactory()

    ####################################################################################
    #                               HELPER METHODS                                     #
    ####################################################################################
    def create_image(self, title="dummy_image",
                     image_url="http://dummyserver.org/images/dummy_image.png",
                     location="/home/foo/dummy_image.png"):
        return Image.objects.create(title=title,
                                    image_url=image_url,
                                    created_on=timezone.now(),
                                    location=location)

    ####################################################################################
    #                                    TESTS                                         #
    ####################################################################################
    def test_image_creation(self):
        image = self.create_image()
        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.__str__(), image.title)

    def test_image_list_view(self):
        image = self.create_image()
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str.encode(image.title), response.content)

    def test_file_with_images_returns_images(self):
        # Generate a test folder to save images
        test_file = settings.BASE_DIR + os.path.sep + 'test_images.txt'
        test_image_path = settings.BASE_DIR + os.path.sep + 'test_saved_images' + os.path.sep
        os.makedirs(test_image_path)
        save_latest_images(test_file, test_image_path)
        # Make sure 6 images were created
        self.assertEqual(len(Image.objects.all()), 6)
        # Remove the test folder
        shutil.rmtree(test_image_path)
