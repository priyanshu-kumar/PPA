# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ppa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='sop_answer',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AddField(
            model_name='project',
            name='sop_question',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
