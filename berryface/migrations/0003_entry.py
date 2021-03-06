# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('berryface', '0002_auto_20180615_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('date', models.DateTimeField()),
                ('measure_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berryface.MeasureType')),
                ('sensor_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berryface.SensorType')),
            ],
        ),
    ]
