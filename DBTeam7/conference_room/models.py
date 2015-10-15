from django.db import models
from django.contrib import auth

class Reservation(models.Model):
    reservation_id= models.AutoField(primary_key=True)
    time = models.DateTimeField()
    recurring = models.BooleanField(default=False)
    user = models.ForeignKey(auth.models.User)

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    capacity = models.IntegerField(default=0)
    reservation = models.ForeignKey(Reservation)

class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room)

class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=45)
    floor = models.ForeignKey(Floor)

class Address(models.Model):
    address = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building)

class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    quantity = models.IntegerField(default=0)
    room = models.ForeignKey(Room)


