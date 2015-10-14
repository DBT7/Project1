# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr_resource', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='conference_room',
            field=models.ForeignKey(default=b'Johnson', to='cr_resource.ConferenceRoom'),
        ),
    ]
