# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-02 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_faq_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='session',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=models.CharField(default='Please wait for your question to be answered', max_length=512),
        ),
    ]
