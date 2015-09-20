from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the cr_resource index.")

def detail(request, conference_room_name):
    return HttpResponse(conference_room_name)

