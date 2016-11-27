from django.db import models


class Image(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    title = models.CharField("Title", max_length=255)
    image_url = models.URLField(
        "Image URL", max_length=255, help_text="The URL to the image file itself")
    location = models.CharField("Path", max_length=255)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title
