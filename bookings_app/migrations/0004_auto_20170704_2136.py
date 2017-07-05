# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings_app', '0003_auto_20170704_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='therapist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings_app.Therapist'),
        ),
    ]