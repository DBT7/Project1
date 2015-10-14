# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conference_room_name', models.CharField(max_length=15)),
                ('conference_room_seating', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(verbose_name=b'date created')),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceRoomResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.CharField(max_length=15)),
                ('resource_qty', models.IntegerField(default=0)),
                ('conference_room', models.ForeignKey(to='cr_resource.ConferenceRoom')),
            ],
        ),
    ]
