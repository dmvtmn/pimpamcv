# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0007_auto_20150527_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='indoc',
            field=models.ForeignKey(related_name=b'doc inicial', default=1, blank=True, to='ppcv.UsrDoc', null=True),
        ),
        migrations.AlterField(
            model_name='revision',
            name='outdoc',
            field=models.ForeignKey(related_name=b'doc final', default=1, blank=True, to='ppcv.UsrDoc', null=True),
        ),
    ]
