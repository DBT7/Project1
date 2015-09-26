from django.shortcuts import render
from django.http import HttpResponse
from .models import ConferenceRoom

def index(request):
    latest_room_list = ConferenceRoom.objects.order_by('-conference_room_seating')[:5]
    output = ', '.join([p.conference_room_name for p in latest_room_list])
    return HttpResponse(output)

def detail(request, conference_room_name):
    return HttpResponse("Your looking at conference room : {}".format(conference_room_name))


