# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Path', default=datetime.datetime(2016, 11, 26, 21, 34, 39, 54012, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
