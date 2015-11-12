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


class Address(models.Model):
    address = models.CharField(db_column='Address', primary_key=True, max_length=45)  # Field name made lowercase.
    building_building = models.ForeignKey('Building', db_column='Building_Building_id')  # Field name made lowercase.

    class Meta:

        
        db_table = 'address'


class Admin(models.Model):
    admin_id = models.IntegerField(db_column='Admin_id', primary_key=True)  # Field name made lowercase.
    person_person = models.ForeignKey('Person', db_column='Person_Person_id')  # Field name made lowercase.

    class Meta:
      
        db_table = 'Admin'


class Building(models.Model):
    building_id = models.AutoField(db_column='Building_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'building'


class Manager(models.Model):
    manager_id = models.IntegerField(db_column='Manager_id', primary_key=True)  # Field name made lowercase.
    admin_admin = models.ForeignKey(Admin, db_column='Admin_Admin_id')  # Field name made lowercase.
    person_person = models.ForeignKey('Person', db_column='Person_Person_id')  # Field name made lowercase.

    class Meta:
        
        db_table = 'Manager'



class Duration(models.Model):
    duration_id = models.AutoField(db_column='Duration_id', primary_key=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'duration'


class Organization(models.Model):
    organization_id = models.AutoField(db_column='Organization_id', primary_key=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='OrgName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'organization'


class Person(models.Model):
    person_id = models.IntegerField(db_column='Person_id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Person'


class Recurrence(models.Model):
    recurrence_id = models.AutoField(db_column='Recurrence_id', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    reservation_reservation = models.ForeignKey('Reservation', db_column='Reservation_Reservation_id', blank=True, null= True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'recurrence'



class Reservation(models.Model):
    reservation_id = models.AutoField(db_column='Reservation_id', primary_key=True)  # Field name made lowercase.
    reservation_dt = models.DateTimeField(db_column='Reservation_dt')  # Field name made lowercase.

         
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    user_user = models.ForeignKey(auth.models.User)  # Field name made lowercase.
    room_room = models.ForeignKey('Room', db_column='Room_Room_id')  # Field name made lowercase.
    room_building_building = models.ForeignKey('Room', db_column='Room_Building_Building_id',
         related_name='reservation_room', blank=True, null=True)  # Field name made lowercase


    

    class Meta:
        
        db_table = 'reservation'


class Resource(models.Model):
    room_room = models.ForeignKey('Room', db_column='Room_Room_id',related_name="res_room")  # Field name made lowercase.
    room_building_building = models.ForeignKey('Room', db_column='Room_Building_Building_id',related_name='res_build')  # Field name made lowercase.
    projector = models.IntegerField(db_column='Projector', blank=True, null=True)  # Field name made lowercase.
    internet = models.IntegerField(db_column='Internet', blank=True, null=True)  # Field name made lowercase.
    handicap_access = models.IntegerField(db_column='Handicap Access', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chalkboard = models.IntegerField(db_column='Chalkboard', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Resource'
        unique_together = ['room_room', 'room_building_building']

   

    class Meta:
        db_table = 'reservation'


class Resource(models.Model):
    resouce_id = models.AutoField(db_column='Resouce_id', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    room_room = models.ForeignKey('Room', db_column='Room_Room_id', related_name='resource_room')  # Field name made lowercase.
    room_building_building = models.ForeignKey('Room', db_column='Room_Building_Building_id')  # Field name made lowercase.

    class Meta:
        db_table = 'resource'



class Room(models.Model):
    room_id = models.IntegerField(db_column='Room_id')  # Field name made lowercase.

    building_building = models.ForeignKey(Building, db_column='Building_Building_id', related_name='room_building' )  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity')  # Field name made lowercase.

    class Meta:
        db_table = 'room'
        unique_together = (('room_id', 'building_building'),)



class User(models.Model):
    user_id = models.IntegerField(db_column='User_id', primary_key=True)  # Field name made lowercase.
    activereservations = models.IntegerField(db_column='ActiveReservations', blank=True, null=True)  # Field name made lowercase.
    manager_manager = models.ForeignKey(Manager, db_column='Manager_Manager_id')  # Field name made lowercase.
    person_person = models.ForeignKey(Person, db_column='Person_Person_id')  # Field name made lowercase.
    organization_organization = models.ForeignKey(Organization, db_column='Organization_Organization_id')  # Field name made lowercase.

    class Meta:
        
        db_table = 'User'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'

