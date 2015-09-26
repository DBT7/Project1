from django.shortcuts import render, get_object_or_404
from .models import ConferenceRoom


def index(request):
    latest_room_list = ConferenceRoom.objects.order_by('-conference_room_seating')[:5]
    context = {'latest_room_list': latest_room_list,}
    return render(request, 'cr_resource/index.html', context)


def detail(request, conference_room_name):
    conference_room = get_object_or_404(ConferenceRoom ,pk=conference_room_name)
    return render(request, 'cr_resource/detail.html', {'conference_room':conference_room})
