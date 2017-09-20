# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161023_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ImageField(default=b'images/1.jpg', upload_to=b'images/'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.date(2017, 8, 30), blank=True),
        ),
    ]
