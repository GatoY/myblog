# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-10-01 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', models.TextField(verbose_name='body')),
                ('cre_date', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('modi_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('abstract', models.CharField(blank=True, help_text='optional, default to get 54 characters in body', max_length=54, null=True, verbose_name='abstract')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='views')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='likes')),
            ],
        ),
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
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='text')),
                ('pub_date', models.DateTimeField(verbose_name='published data')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img/twitter')),
                ('twitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.Twitter', verbose_name='Twitter')),
            ],
        ),
        migrations.CreateModel(
            name='Twitterlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='twitteraccount')),
                ('user', models.CharField(max_length=20, verbose_name='twitteruser')),
                ('img', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.AddField(
            model_name='twitter',
            name='twittername',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.Twitterlist', verbose_name='twittername'),
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
