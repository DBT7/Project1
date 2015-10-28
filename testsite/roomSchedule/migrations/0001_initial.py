# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='Address')),
            ],
            options={
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(serialize=False, primary_key=True, db_column='Admin_id')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.IntegerField(serialize=False, primary_key=True, db_column='Building_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
            ],
            options={
                'db_table': 'Building',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('floor_id', models.IntegerField(serialize=False, primary_key=True, db_column='Floor_id')),
                ('building_building', models.ForeignKey(to='roomSchedule.Building', db_column='Building_Building_id')),
            ],
            options={
                'db_table': 'Floor',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.IntegerField(serialize=False, primary_key=True, db_column='Manager_id')),
                ('admin_admin', models.ForeignKey(to='roomSchedule.Admin', db_column='Admin_Admin_id')),
            ],
            options={
                'db_table': 'Manager',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('organization_id', models.IntegerField(serialize=False, primary_key=True, db_column='Organization_id')),
                ('orgname', models.CharField(max_length=45, null=True, db_column='OrgName', blank=True)),
            ],
            options={
                'db_table': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(serialize=False, primary_key=True, db_column='Person_id')),
                ('firstname', models.CharField(max_length=45, null=True, db_column='FirstName', blank=True)),
                ('lastname', models.CharField(max_length=45, null=True, db_column='LastName', blank=True)),
                ('email', models.CharField(max_length=45, null=True, db_column='Email', blank=True)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('recurrence_id', models.IntegerField(serialize=False, primary_key=True, db_column='Recurrence_id')),
                ('description', models.CharField(max_length=45, null=True, db_column='Description', blank=True)),
            ],
            options={
                'db_table': 'Recurrence',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.IntegerField(serialize=False, primary_key=True, db_column='Reservation_id')),
                ('reservation_dt', models.DateTimeField(db_column='Reservation_dt')),
                ('admin_admin', models.ForeignKey(to='roomSchedule.Admin', db_column='Admin_Admin_id')),
                ('manager_manager', models.ForeignKey(to='roomSchedule.Manager', db_column='Manager_Manager_id')),
                ('recurrence_recurrence', models.ForeignKey(to='roomSchedule.Recurrence', db_column='Recurrence_Recurrence_id')),
            ],
            options={
                'db_table': 'Reservation',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('projector', models.IntegerField(serialize=False, primary_key=True, db_column='Projector')),
                ('internet', models.IntegerField(null=True, db_column='Internet', blank=True)),
                ('handicap_access', models.IntegerField(null=True, db_column='Handicap Access', blank=True)),
                ('chalkboard', models.IntegerField(null=True, db_column='Chalkboard', blank=True)),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(serialize=False, primary_key=True, db_column='Room_id')),
                ('name', models.CharField(max_length=45, null=True, db_column='Name', blank=True)),
                ('capacity', models.IntegerField(null=True, db_column='Capacity', blank=True)),
                ('floor_floor', models.ForeignKey(to='roomSchedule.Floor', db_column='Floor_Floor_id')),
            ],
            options={
                'db_table': 'Room',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(serialize=False, primary_key=True, db_column='User_id')),
                ('activereservations', models.IntegerField(null=True, db_column='ActiveReservations', blank=True)),
                ('manager_manager', models.ForeignKey(to='roomSchedule.Manager', db_column='Manager_Manager_id')),
                ('organization_organization', models.ForeignKey(to='roomSchedule.Organization', db_column='Organization_Organization_id')),
                ('person_person', models.ForeignKey(to='roomSchedule.Person', db_column='Person_Person_id')),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='room_room',
            field=models.ForeignKey(to='roomSchedule.Room', db_column='Room_Room_id'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_room',
            field=models.ForeignKey(to='roomSchedule.Room', db_column='Room_Room_id'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_user',
            field=models.ForeignKey(to='roomSchedule.User', db_column='User_User_id'),
        ),
        migrations.AddField(
            model_name='manager',
            name='person_person',
            field=models.ForeignKey(to='roomSchedule.Person', db_column='Person_Person_id'),
        ),
        migrations.AddField(
            model_name='admin',
            name='person_person',
            field=models.ForeignKey(to='roomSchedule.Person', db_column='Person_Person_id'),
        ),
        migrations.AddField(
            model_name='address',
            name='building_building',
            field=models.ForeignKey(to='roomSchedule.Building', db_column='Building_Building_id'),
        ),
    ]
