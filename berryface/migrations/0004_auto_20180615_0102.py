# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berryface', '0003_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='measure_type_id',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='sensor_type_id',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
    ]