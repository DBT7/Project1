# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr_resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoomResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource_name', models.CharField(max_length=15)),
                ('resource_qty', models.IntegerField(default=0)),
                ('conference_room', models.ForeignKey(to='cr_resource.ConferenceRoom')),
            ],
        ),
        migrations.RemoveField(
            model_name='conferenceroomreasource',
            name='conference_room',
        ),
        migrations.DeleteModel(
            name='ConferenceRoomReasource',
        ),
    ]
