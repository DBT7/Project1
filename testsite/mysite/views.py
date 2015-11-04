'''
Created on Sep 29, 2015

@author: junchuan
'''
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Template, Context
import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, views
from django.conf import settings
from django.shortcuts import redirect
#from mysite.settings import TEMPLATE_DIRS



def current_datetime(request):
    now = datetime.datetime.now()
   # html = "<html><body>It is now %s.</body></html>" % now
    
    t=get_template('mytemp1.html',Template)
   
    html=t.render(Context({'current_date':now}))
    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)





# TODO ADD the following to all of the Views to require a login
def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active():
            login(request,user)

def login_success(request):
    if request.user.groups.filter(name="admin").exists():
        return redirect('admin_home')
    elif request.user.groups.filter(name="manager").exists():
        return redirect('manager_home')
    else:
        return redirect('user_home')

def logout(request):
    logout(request)
    # Redirect to a success page

def password_change(request):
    template_response=views.password_change(request)
    # Do something with the template response
    return  template_response

def password_change_done(request):
    template_response=views.password_change_done(request)
    # Do something with the template response
    return  template_response

def password_reset(request):
    template_response=views.password_reset(request)
    # Do something with the template response
    return  template_response

def password_reset_done(request):
    template_response=views.password_reset_done(request)
    # Do something with the template response
    return  template_response

def password_reset_confirm(request):
    template_response=views.password_reset_confirm(request)
    # Do something with the template response
    return  template_response

def  password_reset_complete(request):
    template_response=views.password_reset_complete(request)
    # Do something with the template response
    return  template_response