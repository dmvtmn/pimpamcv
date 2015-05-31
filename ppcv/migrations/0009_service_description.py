# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0008_auto_20150527_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=2000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
