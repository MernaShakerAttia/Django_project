# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:24
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_contant', models.TextField()),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 6, 125465))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='forbidden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rude_words', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('contant', models.TextField()),
                ('post_time', models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 6, 124615))),
                ('post_image', models.ImageField(blank=True, upload_to=b'./static/img/')),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeks.category')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_contant', models.TextField()),
                ('reply_date', models.DateTimeField(default=datetime.datetime(2017, 2, 10, 19, 24, 6, 126121))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeks.Comment')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeks.Post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_comment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geeks.Post'),
        ),
    ]
