from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

from django.contrib.auth import authenticate, login, views
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from models import *
from django import forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
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

#
# CREATE USER VIEWS
#

class UserList(ListView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('reservation_user_create')

# Functions of this view - Create the user in the reservationuser table
#                        - Hash the users password so that it will work in the login screen
#                        - Add the user to the user group
class ReservationUserCreate(CreateView):
    model = ReservationUser
    fields = []
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        # Get the next autoincrement value and subtract 1 to get the last created user
        user =  User.objects.get(pk = (self.get_next_autoincrement(User) - 1))

        # Reset the password to a hashed value so that the user can login to the tool
        user.set_password(user.password)
        user.save()

        # Add the user to the user group
        user_group = Group.objects.get(name = 'User')
        user_group.user_set.add(user)

        # Complete the form to save valid objects into the database
        form.instance.user = user
        form.instance.user_manager = Manager.objects.get(manager =self.request.user)

        return super(ReservationUserCreate, self).form_valid(form)


    # Get the next value that will be AutoIncremented
    def get_next_autoincrement(self, Model):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute( "SELECT Auto_increment FROM information_schema.tables WHERE table_name='%s';" % \
                        Model._meta.db_table)
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])

#
# Create Manager
#

class ManagerCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('reservation_manager_create')

# Functions of this view - create entry in the manager table
#                        - rehash the managers password so they can login to the tool
#                        - add the manager to the manager group

class ReservationManagerCreate(CreateView):
    model = Manager
    fields = []
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        # Get the next autoincrement value and subtract 1 to get the last created user
        manager =  User.objects.get(pk = (self.get_next_autoincrement(User) - 1))

        # Reset the password to a hashed value so that the user can login to the tool
        manager.set_password(manager.password)
        manager.save()

        # Add the manager to the manager group
        manager_group = Group.objects.get(name='Manager')
        manager_group.user_set.add(manager)

        # Complete the form to save a valid entry into the database
        form.instance.manager = manager
        form.instance.manager_admin = Admin.objects.get(admin =self.request.user)

        return super(ReservationManagerCreate, self).form_valid(form)


    # Get the next value that will be AutoIncremented
    def get_next_autoincrement(self, Model):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute( "SELECT Auto_increment FROM information_schema.tables WHERE table_name='%s';" % \
                        Model._meta.db_table)
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])


#
# Create Admim
#

class AdminCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('reservation_admin_create')

# Functions of this view - create entry into the admin table
#                        - rehash the managers password so that they can login to the tool
#                        - add the admin to the admin group

class ReservationAdminCreate(CreateView):
    model = Admin
    fields = []
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        # Get the last created user object
        admin = User.objects.get(pk = self.get_next_autoincrement(User)-1)

        # Reset the password to a hashed value so that the user can login to the tool
        admin.set_password(admin.password)
        admin.save()

        # Add the admin to the admin group
        admin_group = Group.objects.get(name = 'admin')
        admin_group.user_set.add(admin)

        # Complete the form so to save a valid entry into the database
        form.instance.admin = admin

        return super(ReservationAdminCreate, self).form_valid(form)


    # Get the next value that will be AutoIncremented
    def get_next_autoincrement(self, Model):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute( "SELECT Auto_increment FROM information_schema.tables WHERE table_name='%s';" % \
                        Model._meta.db_table)
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])
class AdminUserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('reservation_admin_user_create')

class ReservationAdminUserCreate(CreateView):
    model = ReservationUser
    fields = ["user_manager"]
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
         # Get the next autoincrement value and subtract 1 to get the last created user
        user =  User.objects.get(pk = (self.get_next_autoincrement(User) - 1))

        # Reset the password to a hashed value so that the user can login to the tool
        user.set_password(user.password)
        user.save()

        # Add the user to the user group
        user_group = Group.objects.get(name = 'User')
        user_group.user_set.add(user)

        # Complete the form to save valid objects into the database
        form.instance.user = user
        print "InFormValid"
        return super(ReservationAdminUserCreate, self).form_valid(form)

    def get_next_autoincrement(self, Model):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute( "SELECT Auto_increment FROM information_schema.tables WHERE table_name='%s';" % \
                        Model._meta.db_table)
        row = cursor.fetchone()
        cursor.close()
        return int(row[0])
