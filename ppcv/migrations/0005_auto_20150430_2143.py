# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0004_auto_20150423_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usrdoc',
            name='category',
            field=models.ForeignKey(related_name=b'type', default=1, verbose_name=b'Tipo de documento', blank=True, to='ppcv.Category'),
        ),
    ]
