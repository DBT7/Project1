from django.db import models

class ConferenceRoom(models.Model):

    def __unicode__(self):
        return self.conference_room_name

    # The name of the conference room
    conference_room_name = models.CharField(max_length=15)
    # The amount of seating in the conference room
    conference_room_seating = models.IntegerField(default=0)
    # The Date the conference room was created
    created_date = models.DateTimeField('date created')
    # The conference room schedule

class ConferenceRoomResource(models.Model):

    def __unicode__(self):
        return self.resource_name

    # The conference room the resource belongs to.
    conference_room=models.ForeignKey(ConferenceRoom)
    # The name of the resource
    resource_name=models.CharField(max_length=15)
    # The number of resources
    resource_qty = models.IntegerField(default=0)

