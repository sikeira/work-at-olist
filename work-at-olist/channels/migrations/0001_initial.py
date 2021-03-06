# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.Channel')),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.ChannelCategory')),
            ],
        ),
    ]
