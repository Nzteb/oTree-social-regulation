# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-19 07:48
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='mturk_expiration',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
