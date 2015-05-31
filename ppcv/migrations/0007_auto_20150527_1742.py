# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0006_remove_usrdoc_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='indoc',
            field=models.ForeignKey(related_name=b'doc inicial', default=1, blank=True, to='ppcv.UsrDoc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='revision',
            name='outdoc',
            field=models.ForeignKey(related_name=b'doc final', default=1, blank=True, to='ppcv.UsrDoc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='revision',
            name='service',
            field=models.OneToOneField(related_name=b'revision', to='ppcv.Service'),
        ),
        migrations.AlterField(
            model_name='usrdoc',
            name='user',
            field=models.ForeignKey(related_name=b'autor', default=1, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
