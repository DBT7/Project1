'''
Created on Sep 29, 2015

@author: junchuan
'''
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Template, Context
import datetime
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



from django.shortcuts import render

import MySQLdb

