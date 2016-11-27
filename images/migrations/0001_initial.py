# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('image_url', models.URLField(max_length=255, help_text='The URL to the image file itself', verbose_name='Image URL')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ['-created_on', 'title'],
                'verbose_name': 'Image',
            },
        ),
    ]
