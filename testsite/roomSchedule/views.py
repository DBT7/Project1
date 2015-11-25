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

class ReservationList(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.exclude(user_user = 1).exclude(reservation_dt__lte = datetime.now())

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationList, self).dispatch(request,*args, **kwargs)


class ReservationDetail(DetailView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'user_user', 'room_room']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationDetail, self).dispatch(request,*args, **kwargs)

class ReservationCreate(CreateView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'room_room', 'reservation_comment_id']
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
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationUpdate, self).dispatch(request,*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_user = self.request.user
        return super(ReservationUpdate, self).form_valid(form)

class ReservationDelete(UpdateView):
    model=Reservation
    success_url=reverse_lazy('home')
    fields = []

    def send_email_waitlist(self, user):
        # Send Email to person on waitlist
        print 'Sending email to user: {} that is on the waitlist'.format(user)

    def form_valid(self, form):

        # Set the Reservation back to a blank reservation
        form.instance.user_user = User.objects.get(pk=1)

        # See if that reservation is on the waitlist
        try:
            waitlist =WaitList.objects.get(reservation = "{}".format(form.instance.reservation_id))
        except:
            # There is not anyone on the waitlist to match that query
            waitlist = None

        # If it was on the Waitlist then send it to the users for that room on the list
        if waitlist is not None:
            for row in waitlist:
                self.send_email_waitlist(row.user)
        return super(ReservationDelete, self).form_valid(form)

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

class AvailableReservationList(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(room_room=self.kwargs['room']).filter(user_user = 1).exclude(reservation_dt__lte = datetime.now())

class ReservedReservationList(ListView):
    model = Reservation

    def get_queryset(self):
        return Reservation.objects.filter(room_room=self.kwargs['room']).exclude(user_user = 1).exclude(reservation_dt__lte = datetime.now())
#
# RESOURCE VIEWS
#
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
    success_url = reverse_lazy('home')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceCreate, self).dispatch(request, *args, **kwargs)

class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['resource_id', 'title', 'description']
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceUpdate, self).dispatch(request, *args, **kwargs)

class ResourceDelete(DeleteView):
    model = Resource
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResourceDelete, self).dispatch(request, *args, **kwargs)

#
# ROOM VIEWS
#

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
    success_url = reverse_lazy('home')

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

class CommentForm(forms.Form):
    text = forms.CharField(
        label="Comment",
        max_length=1024,
        widget=forms.Textarea)
    rank = forms.ChoiceField(choices=Comment.RANK_CHOICES)

#
# COMMENT VIEWS
#

class CommentList(ListView):
    model = Comment

    # adding a form to a listview
    def get_context_data(self, **kwargs):
        form = CommentForm
        context = super(CommentList, self).get_context_data(**kwargs)
        context['form'] = form
        return context

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = ['text', 'rank']
    success_url = reverse_lazy('home')

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['text', 'rank']
    success_url = reverse_lazy('home')
    #def get_object():

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')

#
# WAITLIST VIEWS
#

class WaitListList(ListView):
    model = WaitList

class WaitListUpdate(UpdateView):
    model = WaitList

class WaitListCreate(CreateView):
    model=WaitList

class WaitListDetail(DetailView):
    model = DeleteView



