# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-25 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATTIC_APP', '0012_junk_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junk',
            name='image',
            field=models.ImageField(default='ATTIC_APP/images/onigiri.png', upload_to='ATTIC_APP/images'),
        ),
    ]
