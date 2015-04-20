# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppcv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(default=0.0, max_digits=50, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_code', models.CharField(unique=True, max_length=6)),
                ('description', models.CharField(max_length=120, null=True, blank=True)),
                ('discount_value', models.DecimalField(default=0.25, max_digits=100, decimal_places=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, to='checkout.Coupon', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='service',
            field=models.ForeignKey(blank=True, to='ppcv.Service', null=True),
            preserve_default=True,
        ),
    ]
