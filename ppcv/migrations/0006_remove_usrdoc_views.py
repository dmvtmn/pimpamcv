# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0005_auto_20150430_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usrdoc',
            name='views',
        ),
    ]
