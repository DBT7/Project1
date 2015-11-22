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

from roomSchedule import views



urlpatterns = [
    # Login, logout and change password view urls
    url('^', include('django.contrib.auth.urls')),

    # Home Page urls
    url(r'^home/', login_success, name='home'),
    url(r'^user/$',views.UserHome.as_view(template_name="roomSchedule/reservation_list.html"), name='user_home'),
    url(r'^manager/$',views.UserHome.as_view(template_name="roomSchedule/reservation_list_manager.html"), name='manager_home'),
    url(r'^admin/$',views.UserHome.as_view(template_name="roomSchedule/reservation_list_admin.html"), name='admin_home'),

    # Reservation urls
    url(r'^pastreservation/$',views.PastReservations.as_view(template_name = "roomSchedule/past_reservations_list.html"), name='past_reservations'),
    url(r'^(?P<pk>[0-9]+)/detailreservation$', views.ReservationDetail.as_view(), name='reservation_detail'),
    url(r'createreservation/$', views.ReservationCreate.as_view(), name='reservation_create'),
    #url(r'(?P<room>\w+)/create/$', views.ReservationCreate.as_view(), name='reservation_create'),
    url(r'^(?P<pk>[0-9]+)/updatereservation/$', views.ReservationUpdate.as_view(), name='reservation_edit'),
    url(r'^(?P<pk>[0-9]+)/deletereservation/$', views.ReservationDelete.as_view(), name='reservation_delete'),
    url(r'^(?P<room>\w+)/availablereservation/$', views.AvailableReservationList.as_view(template_name='roomSchedule/reservation_list_available_times.html'), name='available_reservations' ),

    # Resource urls
    url(r'^resource/$',views.ResourceList.as_view(template_name = "Resource/resource_list.html"), name='resource_list'),
    url(r'^(?P<pk>[0-9]+)/detailresource/$', views.ResourceDetail.as_view(template_name = "Resource/resource_detail.html"), name='resource_detail'),
    url(r'^createresource/$', views.ResourceCreate.as_view(template_name = "Resource/resource_form.html"), name='resource_create'),
    url(r'^(?P<pk>[0-9]+)/updateresource/$', views.ResourceUpdate.as_view(template_name = "Resource/resource_form.html"), name = 'resource_update'),
    url(r'^(?P<pk>[0-9]+)/deleteresoure/$', views.ResourceDelete.as_view(template_name = "Resource/resource_confirm_delete.html"), name='resource_delete'),


    # Room urls
    url(r'^(?P<resource>\w+)/room/$', views.RoomListFromResource.as_view(template_name = "Room/room_list.html"), name='room_list_from_resource' ),
    url(r'^room/$', views.RoomList.as_view(template_name = "Room/room_list.html"), name='room_list' ),
    url(r'^(?P<pk>[0-9]+)/detailroom/$', views.RoomDetail.as_view(template_name = "Room/room_detail.html"),name = 'room_detail'),
    url(r'^createroom/$', views.RoomCreate.as_view(template_name = "Room/room_form.html"), name = 'room_create'),
    url(r'^(?P<pk>[0-9]+)/updateroom/$', views.RoomUpdate.as_view(template_name = "Room/room_form.html"), name = "room_update"),
    url(r'^(?P<pk>[0-9]+)/deleteroom/$', views.RoomDelete.as_view(template_name = "Room/room_confirm_delete.html"), name = "room_delete"),


    # Django adminsite urls
    url(r'^adminsite/', include(admin.site.urls)),

    # Other urls
    url(r'^hello/$', hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search_form/$',views.search_form),
    url(r'^search/$',views.search),

    

]
