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
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(serialize=False, primary_key=True, db_column='Building_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('text', models.TextField(max_length=1024, null=True, blank=True)),
                ('rank', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('manager_admin', models.ForeignKey(to='roomSchedule.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(serialize=False, primary_key=True, db_column='Reservation_id')),
                ('reservation_dt', models.DateTimeField(db_column='Reservation_dt')),
                ('duration', models.IntegerField(null=True, db_column='Duration', blank=True)),
                ('reservation_comment_id', models.ForeignKey(to='roomSchedule.Comment', db_column='reservation_comment_id')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
        migrations.CreateModel(
            name='ReservationUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('user_manager', models.ForeignKey(to='roomSchedule.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.AutoField(serialize=False, primary_key=True, db_column='Resource_id')),
                ('title', models.CharField(max_length=200, null=True, db_column='Title', blank=True)),
                ('description', models.CharField(max_length=45, null=True, db_column='Description', blank=True)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(serialize=False, primary_key=True, db_column='Room_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
                ('capacity', models.IntegerField(db_column='Capacity')),
                ('building_building', models.ForeignKey(related_name='room_building', db_column='Building_Building_id', to='roomSchedule.Building')),
                ('resource', models.ManyToManyField(to='roomSchedule.Resource')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='WaitList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reservation', models.ForeignKey(to='roomSchedule.Reservation')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_room',
            field=models.ForeignKey(to='roomSchedule.Room', db_column='Room_Room_id'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
