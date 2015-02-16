# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150211_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(upload_to='avatars', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postfile',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='files'),
            preserve_default=True,
        ),
    ]
