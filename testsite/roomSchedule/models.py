# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib import auth

class Building(models.Model):
    building_id = models.AutoField(db_column='Building_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'building'


class Reservation(models.Model):
    reservation_id = models.AutoField(db_column='Reservation_id', primary_key=True)  # Field name made lowercase.
    reservation_dt = models.DateTimeField(db_column='Reservation_dt')  # Field name made lowercase.

    # TODO - remove and fix rest of code - not needed for new layout
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    user_user = models.ForeignKey(auth.models.User, blank=True, null=True)  # Field name made lowercase.
    room_room = models.ForeignKey('Room', db_column='Room_Room_id')  # Field name made lowercase.
    reservation_comment_id = models.ForeignKey('Comment', db_column='reservation_comment_id')

    class Meta:
        
        db_table = 'reservation'


class Resource(models.Model):
    resource_id = models.AutoField(db_column='Resource_id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'resource'


class Room(models.Model):
    room_id = models.AutoField(db_column='Room_id', primary_key=True)  # Field name made lowercase.
    building_building = models.ForeignKey(Building, db_column='Building_Building_id', related_name='room_building' )  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.
    resource = models.ForeignKey(Resource, blank=True, null=True)
    class Meta:
        db_table = 'room'


class Comment(models.Model):
    NOT_ACCEPTABLE = 1
    SLIGHTLY_ACCEPTABLE =2
    MODERATELY_ACCEPTABLE = 3
    VERY_ACCEPTABLE=4
    COMPLETELY_ACCEPTABLE=5
    RANK_CHOICES = (
        (NOT_ACCEPTABLE, 'Not Acceptable'),
        (SLIGHTLY_ACCEPTABLE, 'Slightly Acceptable'),
        (MODERATELY_ACCEPTABLE, 'Moderately Acceptable'),
        (VERY_ACCEPTABLE, 'Very Acceptable'),
        (COMPLETELY_ACCEPTABLE, 'Completely Acceptable')
    )

    comment_id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=1024, blank=True, null=True)
    rank = models.IntegerField(blank= True, null=True)

    class Meta:

        db_table = 'comment'

class WaitList(models.Model):
    user = models.ForeignKey(auth.models.User)
    reservation = models.ForeignKey(Reservation)

class Admin(models.Model):
    admin = models.ForeignKey(auth.models.User)

class Manager(models.Model):
    manager = models.ForeignKey(auth.models.User)
    manager_admin = models.ForeignKey(Admin)

class ReservationUser(models.Model):
    user = models.ForeignKey(auth.models.User)
    user_manager = models.ForeignKey(Manager)