from django.contrib import admin
from .models import *

class ResourceInLine(admin.StackedInline):
    model = Resource
    extra = 1

class FloorInline(admin.StackedInline):
    model = Floor
    extra = 0

class RoomInline(admin.StackedInline):
    model = Room
    extra = 0

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name']}),
        ('Max Seating', {'fields': ['capacity']})
    ]
    inlines = [ResourceInLine, FloorInline]

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Reservation Holder', { 'fields': ['user']}),
        ('Time Reserved',      { 'fields': ['time']}),
        ('Recurring',          { 'fields': ['recurring'], 'classes': ['collapse']})
    ]
    inlines = [RoomInline]

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)