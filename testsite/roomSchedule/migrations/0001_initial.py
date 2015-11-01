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
                ('address', models.CharField(max_length=45, serialize=False, primary_key=True, db_column='Address')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.IntegerField(serialize=False, primary_key=True, db_column='Building_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('duration_id', models.IntegerField(serialize=False, primary_key=True, db_column='Duration_id')),
                ('duration', models.IntegerField(null=True, db_column='Duration', blank=True)),
            ],
            options={
                'db_table': 'duration',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_id', models.IntegerField(serialize=False, primary_key=True, db_column='Organization_id')),
                ('orgname', models.CharField(max_length=45, null=True, db_column='OrgName', blank=True)),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('recurrence_id', models.IntegerField(serialize=False, primary_key=True, db_column='Recurrence_id')),
                ('description', models.CharField(max_length=45, null=True, db_column='Description', blank=True)),
            ],
            options={
                'db_table': 'recurrence',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.IntegerField(serialize=False, primary_key=True, db_column='Reservation_id')),
                ('reservation_dt', models.DateTimeField(db_column='Reservation_dt')),
                ('duration', models.IntegerField(null=True, db_column='Duration', blank=True)),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resouce_id', models.IntegerField(serialize=False, primary_key=True, db_column='Resouce_id')),
                ('description', models.CharField(max_length=45, null=True, db_column='Description', blank=True)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_id', models.IntegerField(db_column='Room_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
                ('capacity', models.IntegerField(db_column='Capacity')),
                ('building_building', models.ForeignKey(related_name='room_building', db_column='Building_Building_id', to='roomSchedule.Building')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='room_building_building',
            field=models.ForeignKey(to='roomSchedule.Room', db_column='Room_Building_Building_id'),
        ),
        migrations.AddField(
            model_name='resource',
            name='room_room',
            field=models.ForeignKey(related_name='resource_room', db_column='Room_Room_id', to='roomSchedule.Room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_building_building',
            field=models.ForeignKey(related_name='reservation_room', db_column='Room_Building_Building_id', blank=True, to='roomSchedule.Room', null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_room',
            field=models.ForeignKey(to='roomSchedule.Room', db_column='Room_Room_id'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recurrence',
            name='reservation_reservation',
            field=models.ForeignKey(db_column='Reservation_Reservation_id', blank=True, to='roomSchedule.Reservation', null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='building_building',
            field=models.ForeignKey(to='roomSchedule.Building', db_column='Building_Building_id'),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together=set([('room_id', 'building_building')]),
        ),
    ]
