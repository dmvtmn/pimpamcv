# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('poster', models.ForeignKey(related_name=b'poster', default=1, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('rating', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('price', models.DecimalField(default=29.99, max_digits=10, decimal_places=2)),
                ('sale_price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('service', models.OneToOneField(primary_key=True, serialize=False, to='ppcv.Service')),
                ('image', models.FileField(null=True, upload_to=b'services/images/')),
                ('featured', models.BooleanField(default=False)),
                ('thumbnail', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsrDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('attachment', models.FileField(null=True, upload_to=b'attachments', blank=True)),
                ('description', models.TextField(null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(related_name=b'type', default=1, blank=True, to='ppcv.Category')),
                ('user', models.ForeignKey(related_name=b'owner', default=1, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='revision',
            name='service',
            field=models.ForeignKey(related_name=b'revision', default=1, blank=True, to='ppcv.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='revision',
            name='user',
            field=models.ForeignKey(related_name=b'lister', default=1, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='revision',
            field=models.ForeignKey(to='ppcv.Revision'),
            preserve_default=True,
        ),
    ]
