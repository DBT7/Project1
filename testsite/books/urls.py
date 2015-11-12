from django.conf.urls import url

from . import views
from django.conf.urls.i18n import urlpatterns

urlpatterns=[
             url(r'^$',views.display_meta,name='display_meta'),
             ]