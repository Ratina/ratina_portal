# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150211_0626'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogFile',
            new_name='PostFile',
        ),
    ]
