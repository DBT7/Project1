from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

from django.contrib.auth import authenticate, login, views
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from models import *
from django import forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Reservation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy, reverse
from datetime import datetime, timedelta

# Create your views here.

def search_form(request):
    
    return render(request,'search_form.html')

def search(request):
    if 'q' in request.GET:
        message="You searched for:%r" % request.GET['q']
    else:
        message="You didn't specify any search criteria"
    return HttpResponse(message)

class AdminHome(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user_user = self.request.user).exclude(reservation_dt__lte = datetime.now())

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminHome, self).dispatch(request,*args, **kwargs)

class ManagerHome(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user_user = self.request.user).exclude(reservation_dt__lte = datetime.now())

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ManagerHome, self).dispatch(request,*args, **kwargs)

class UserHome(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(user_user = self.request.user).exclude(reservation_dt__lte = datetime.now())

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserHome, self).dispatch(request,*args, **kwargs)

class ReservationDetail(DetailView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'user_user', 'room_room']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationDetail, self).dispatch(request,*args, **kwargs)

class ReservationCreate(CreateView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'room_room']
    success_url = reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationCreate, self).dispatch(request,*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_user = self.request.user
        return super(ReservationCreate, self).form_valid(form)

class ReservationUpdate(UpdateView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'room_room']
    success_url = reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationUpdate, self).dispatch(request,*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_user = self.request.user
        return super(ReservationUpdate, self).form_valid(form)

class ReservationDelete(DeleteView):
    model=Reservation
    success_url=reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationDelete, self).dispatch(request,*args, **kwargs)

class PastReservations(ListView):
    model = Reservation
    template_name =  'roomSchedule/past_reservations_list.html'

    def get_queryset(self):
        return Reservation.objects.filter(user_user = self.request.user).exclude(reservation_dt__gte = datetime.now())

    def get_template_names(self):
          return self.template_name

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PastReservations, self).dispatch(request,*args, **kwargs)

# Would work if we put in a bunch of blank reservations for each of the rooms.
# Each time a room is created it would have to create all of the blank reservations.
class AvailableReservationList(ListView):
    model = Reservation

    def get_queryset(self):
        #return Reservation.objects.filter(room_room=self.kwargs['room']).filter(user_user=None).exclude(reservation_dt__lte=datetime.now()).exclude(reservation_dt__gte=datetime.now()+timedelta(days = 1))
        return Reservation.objects.filter(room_room=self.kwargs['room']).exclude(reservation_dt__lte = datetime.now())#.exclude(reservation_dt__gte=(datetime.now()+timedelta(days = 1)))

# TODO - create views that create, update and delete resources.
# Still have to create the HTML and add to the urls.py

class ResourceForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=45)

# This resource list view can be called the Admin Homepage and When the user is trying to make a reservation
class ResourceList(ListView):
    model = Resource

    def get_queryset(self):
        return Resource.objects.all()

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceList, self).dispatch(request, *args, **kwargs)

class ResourceDetail(DetailView):
    model = Resource
    fields = ['resource_id', 'title', 'description']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceDetail, self).dispatch(request, *args, **kwargs)

class ResourceCreate(CreateView):
    model = Resource
    fields = ['resource_id', 'title', 'description']

    def get_context_data(self, **kwargs):
        form = ResourceForm
        context = super(ResourceCreate, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceCreate, self).dispatch(request, *args, **kwargs)

class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['resource_id', 'title', 'description']
    # TODO - define a success_url
    #success_url


    def dispatch(self, request, *args, **kwargs):
        return super(ResourceUpdate, self).dispatch(request, *args, **kwargs)

class ResourceDelete(DeleteView):
    model = Resource
    # TODO - define a success_url
    #success_url =

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceDelete, self).dispatch(request, *args, **kwargs)


# TODO - there will need to be separate vies for the Room list.
# 1. to be called from the admin page and when the user wants to make a specific reservation based on the room.
#       will be generic and will show all of the room objects
# 2. to be called when the user is making reservations by choosing a reservation first.
#       will filter by using **kwargs
# TODO - create views that will create, update and delete rooms.

class RoomForm(forms.Form):
    building_building=forms.ModelChoiceField(queryset=Building.objects.all())
    name = forms.CharField(max_length=45)
    capacity = forms.IntegerField()
    resource = forms.ModelChoiceField(queryset=Resource.objects.all())

class RoomList(ListView):
    model = Room

    def get_queryset(self):
        return Room.objects.all()

    @method_decorator(login_required)
    def dispach(self, request, *args, **kwargs):
        return super(RoomList, self).dispatch(self,*args, **kwargs)

class RoomListFromResource(ListView):
    model = Room

    def get_queryset(self):
        return Room.objects.filter(resource=self.kwargs['resource'])

    @method_decorator(login_required)
    def dispach(self, request, *args, **kwargs):
        return super(RoomList, self).dispatch(self,*args, **kwargs)

class RoomDetail(DetailView):
    model = Room
    fields = ['room_id', 'building_building', 'name', 'capacity', 'resource']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RoomDetail, self).dispatch(request, *args, **kwargs)

class RoomCreate(CreateView):
    model = Room
    fields = ['room_id', 'building_building', 'name', 'capacity', 'resource']

    def get_context_data(self, **kwargs):
        form = RoomForm
        context = super(RoomCreate, self).get_context_data(**kwargs)
        context['form'] = form
        return context

class RoomUpdate(UpdateView):
    model = Room
    fields = ['room_id', 'building_building', 'name', 'capacity', 'resource']

    # TODO - define a success_url
    #success_url =

    def dispatch(self, request, *args, **kwargs):
        return super(ResourceUpdate, self).dispatch(request, *args, **kwargs)

class RoomDelete(DeleteView):
    model = Room

    # TODO - define a success_url
    #success_url =

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceDelete, self).dispach(request, *args, **kwargs)




