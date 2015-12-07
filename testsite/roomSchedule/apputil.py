
from django.contrib.auth.models import User,Group

import datetime


def generate_report():

    # Not sure how you set up your manager group
    # if you set up your manger group as 'MgrGrp' then this code should work
    # if you have a different name for manager group, change 'MgrGrp' accordingly

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
