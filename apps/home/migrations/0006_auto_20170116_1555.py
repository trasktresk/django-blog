# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_articles_short_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='category_id',
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
