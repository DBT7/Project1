"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from mysite.views import *
from books.views import *

from roomSchedule import views



urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^home/', login_success, name='home'),
    url(r'^user/$',views.UserHome.as_view(), name='user_home'),
    url(r'^manager/$',views.UserHome.as_view(), name='manager_home'),
    url(r'^admin/$',views.UserHome.as_view(), name='admin_home'),
    url(r'^past/$',views.PastReservations.as_view(template_name = "roomSchedule/past_reservations_list.html"), name='past_reservations'),
    url(r'^(?P<pk>[0-9]+)/$', views.ReservationDetail.as_view(), name='reservation_detail'),
    url(r'create/$', views.ReservationCreate.as_view(), name='reservation_create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ReservationUpdate.as_view(), name='reservation_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ReservationDelete.as_view(), name='reservation_delete'),
    url(r'^adminsite/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^meta/$',display_meta),
    url(r'^search_form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^books/',include('books.urls')),
    

]
