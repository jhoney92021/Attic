# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATTIC_APP', '0016_auto_20190725_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junk',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='/images'),
        ),
    ]
