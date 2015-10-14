# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(serialize=False, primary_key=True)),
                ('building_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floor_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(serialize=False, primary_key=True)),
                ('time', models.DateTimeField()),
                ('recurring', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('capacity', models.IntegerField(default=0)),
                ('reservation', models.ForeignKey(to='conference_room.Reservation')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='room',
            field=models.ForeignKey(to='conference_room.Room'),
        ),
        migrations.AddField(
            model_name='floor',
            name='room',
            field=models.ForeignKey(to='conference_room.Room'),
        ),
        migrations.AddField(
            model_name='building',
            name='floor',
            field=models.ForeignKey(to='conference_room.Floor'),
        ),
        migrations.AddField(
            model_name='address',
            name='building',
            field=models.ForeignKey(to='conference_room.Building'),
        ),
    ]
