# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-08-26 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_article_topped'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='cate_name')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='cre_time')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='modi_time')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='lable_name')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='cre_time')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='modi_time')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, help_text='optional, default to get 54 characters in body', max_length=54, null=True, verbose_name='abstract'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.Category', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='apps.Tag', verbose_name='tags group'),
        ),
    ]
