# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-03 18:56
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('fhmp_setup', '0003_auto_20190703_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='CC10_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC11_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC12_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC13_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC14_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC15_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC16_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC2_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC3_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC4_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC5_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC6_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC7_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC8_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
        migrations.AlterField(
            model_name='player',
            name='CC9_ans',
            field=otree.db.models.BooleanField(choices=[[True, 'True'], [False, 'False']]),
        ),
    ]
