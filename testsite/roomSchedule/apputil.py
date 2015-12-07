from .models import *
from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from django.dispatch import receiver

import datetime

def slot_scheduled(request):


    all_resr=Reservation.objects.all()

    return all_resr

def get_user_reservation(request):
    resv_dic={}


    resv_dic['test']=request.user.groups.values_list('name',flat=True)
    return resv_dic


def generate_report():

    managers=User.objects.filter(groups__name='MgrGrp')

    begin_prev_month=datetime.datetime.now()+datetime.timedelta(days=-30)
    for m in managers:
        m_users=User.objects.filter(groups__name=m.username)

        msg=''
        for mu in m_users:
            msg=msg+mu.username+'\n'
            mu_resv=mu.reservation_set.all().filter(reservation_dt__lt=datetime.datetime.now())

            for wr in mu_resv:
                msg=msg+"Time:"+str(wr.reservation_dt) +'\n'
                msg=msg+"Location:"+ str(wr.room_room) +'\n'
                msg=msg+"Duration:"+ str(wr.duration*30) +'mins' +'\n\n'


        m.email_user(subject="You monthly report.",message=msg)
