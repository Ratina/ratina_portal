# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150209_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 9, 5, 55, 59, 241136)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 2, 9, 5, 56, 19, 696832, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
