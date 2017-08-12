# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('trailer', models.CharField(max_length=300)),
            ],
        ),
    ]
