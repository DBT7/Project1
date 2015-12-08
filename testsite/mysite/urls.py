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

    # Manager list urls
    url(r'^managerlist', views.ManagerList.as_view(template_name="Manager/manager_list.html"), name='manager_list'),
    url(r'^(?P<manager>[0-9]+)/reservationbymanager', views.ReservationListByManager.as_view(template_name='roomSchedule/reservation_list_by_manager.html'),name='reservations_by_manager'),
    url(r'^/reservationlistmanager', views.ReservationListManager.as_view(template_name='roomSchedule/reservation_list_by_manager.html'),name='reservations_list_manager'),


    # Reservation urls
    url(r'^allreservations/$', views.ReservationList.as_view(template_name = "roomSchedule/reservation_list_all.html"), name='all_reservations'),
    url(r'^pastreservation/$',views.PastReservations.as_view(template_name = "roomSchedule/past_reservations_list.html"), name='past_reservations'),
    url(r'^(?P<pk>[0-9]+)/detailreservation$', views.ReservationDetail.as_view(), name='reservation_detail'),
    url(r'createreservation/$', views.ReservationCreate.as_view(), name='reservation_create'),
    url(r'^(?P<pk>[0-9]+)/updatereservation/$', views.ReservationUpdate.as_view(), name='reservation_edit'),
    url(r'^(?P<pk>[0-9]+)/deletereservation/$', views.ReservationDelete.as_view(template_name='roomSchedule/reservation_confirm_delete.html' ), name='reservation_delete'),
    url(r'^(?P<room>\w+)/availablereservation/$', views.AvailableReservationList.as_view(template_name='roomSchedule/reservation_list_available_times.html'), name='available_reservations' ),

    # Waitlist urls
    url(r'^(?P<pk>[0-9]+)/createwaitlist/$', views.WaitListCreate.as_view(template_name='Waitlist/waitlist_form.html'), name='waitlist_create'),

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


    # Comment urls
    url(r'^(?P<pk>[0-9]+)/updatecomment/$', views.CommentUpdate.as_view(template_name="Comment/comment_form.html"), name="comment_update"),

    # Create Users URLS

    url(r'^createuser/$', views.UserCreate.as_view(template_name = "User/user_form.html"), name = 'user_create'),
    url(r'^createusersuccess/$', views.ReservationUserCreate.as_view(template_name = "ReservationUser/ReservationUser_form.html"), name = 'reservation_user_create'),

    # Admin Create user urls
    url(r'^admincreateuser/$', views.AdminUserCreate.as_view(template_name = "User/user_form.html"), name = 'admin_user_create'),
    url(r'^admincreateusersuccess/$', views.ReservationAdminUserCreate.as_view(template_name = "Admin/admin_form.html"), name = 'reservation_admin_user_create'),

    # Create Managers usls
    url(r'^createmanager/$', views.ManagerCreate.as_view(template_name = "User/user_form.html"), name = 'manager_create'),
    url(r'^createmanagersuccess/$', views.ReservationManagerCreate.as_view(template_name = "Manager/manager_form.html"), name = 'reservation_manager_create'),

    # Create Admin urls
    url(r'^createadmin/$', views.AdminCreate.as_view(template_name = "User/user_form.html"), name = 'admin_create'),
    url(r'^createadminsuccess/$', views.ReservationAdminCreate.as_view(template_name = "Admin/admin_form.html"), name = 'reservation_admin_create'),

    # Django adminsite urls
    url(r'^adminsite/', include(admin.site.urls)),

    # Other urls
    url(r'^hello/$', hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search_form/$',views.search_form),
    url(r'^search/$',views.search),

    

]
