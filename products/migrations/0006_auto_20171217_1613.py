# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171217_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
