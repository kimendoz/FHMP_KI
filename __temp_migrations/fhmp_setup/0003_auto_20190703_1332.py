# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-03 18:32
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('fhmp_setup', '0002_auto_20190703_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='CC1_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
    ]