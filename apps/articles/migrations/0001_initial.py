# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название статьи')),
                ('create_date', models.DateField(verbose_name='Дата публикации')),
                ('short_text', models.TextField(default='', verbose_name='Аннотация статьи')),
                ('text', models.TextField(default='', verbose_name='Текст статьи')),
            ],
            options={
                'ordering': ['-create_date'],
                'verbose_name_plural': 'Статьи',
                'verbose_name': 'Статья',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Alias категории')),
                ('parent_id', models.IntegerField(default=0, verbose_name='Родительская категории')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Categories'),
        ),
    ]
