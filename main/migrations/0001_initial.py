# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('mainimage', models.ImageField(null=True, upload_to='img')),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ManyToManyField(to='main.ImageModel')),
            ],
        ),
    ]
