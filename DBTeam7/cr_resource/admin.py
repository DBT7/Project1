from django.contrib import admin

from .models import ConferenceRoom, ConferenceRoomResource

class ConferenceRoomResourceInLine(admin.StackedInline):
    model = ConferenceRoomResource
    extra = 1

class ConferenceRoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['conference_room_name']}),
        ('Max Seating',      {'fields': ['conference_room_seating']}),
        ('Date Information', {'fields': ['created_date'], 'classes': ['collapse']})
    ]
    inlines = [ConferenceRoomResourceInLine]

    list_display =  ('conference_room_name', 'conference_room_seating')
    search_fields = ['conference_room_name', 'conference_room_seating']

admin.site.register( ConferenceRoom, ConferenceRoomAdmin)