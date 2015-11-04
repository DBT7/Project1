from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth import authenticate, login, views
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from models import *
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from models import Reservation
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy, reverse
# Create your views here.

def search_form(request):
    return render(request,'search_form.html')

def search(request):
    if 'q' in request.GET:
        message="You searched for:%r" % request.GET['q']
    else:
        message="You didn't specify any search criteria"
    return HttpResponse(message)

# Kept as example of what needs to be done in the homepage so that only the current users reservations are loaded.
def user_homepage(request):
    if not request.user.is_authenticated():
        # If there is not a current session this will allow the user to login then see the page that is requested
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    else:
        object_list = Reservation.objects.filter(user_user=request.user)
        context = {'object_list':object_list}
        return render(request, 'roomSchedule/reservation_list.html', context )

class ReservationForm(forms.Form):
    reservation_dt = forms.DateTimeField()
    duration = forms.IntegerField()
    user_user = forms.ModelChoiceField(queryset=User.objects.all())
    room_room = forms.ModelChoiceField(queryset=Room.objects.all())

class AdminHome(ListView):
    model = Reservation

#TODO - need to bring down the results to just the signed in user. Will be part of the get_context_data
    def get_context_data(self, **kwargs):
        form = ReservationForm
        context = super(AdminHome, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminHome, self).dispatch(request,*args, **kwargs)

class ManagerHome(ListView):
    model = Reservation

#TODO - need to bring down the results to just the signed in user. Will be part of the get_context_data
    def get_context_data(self, **kwargs):
        form = ReservationForm
        context = super(ManagerHome, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ManagerHome, self).dispatch(request,*args, **kwargs)

class UserHome(ListView):
    model = Reservation

#TODO - need to bring down the results to just the signed in user. Will be part of the get_context_data
    def get_context_data(self, **kwargs):
        form = ReservationForm
        context = super(UserHome, self).get_context_data(**kwargs)
        context['form'] = form
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserHome, self).dispatch(request,*args, **kwargs)

class ReservationDetail(DetailView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'user_user', 'room_room', 'room_building_building']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationDetail, self).dispatch(request,*args, **kwargs)

#
class ReservationCreate(CreateView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'user_user', 'room_room', 'room_building_building']
    success_url = reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationCreate, self).dispatch(request,*args, **kwargs)

class ReservationUpdate(UpdateView):
    model=Reservation
    fields = ['reservation_id', 'reservation_dt', 'duration', 'user_user', 'room_room', 'room_building_building']
    success_url = reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationUpdate, self).dispatch(request,*args, **kwargs)


class ReservationDelete(DeleteView):
    model=Reservation
    success_url=reverse_lazy('user_home')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationDelete, self).dispatch(request,*args, **kwargs)