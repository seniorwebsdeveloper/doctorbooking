# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('DOCTOR', 'DOCTOR'), ('PATIENT', 'PATIENT'), ('RECEPTIONIST', 'RECEPTIONIST')], default='PATIENT', max_length=15),
        ),
    ]
