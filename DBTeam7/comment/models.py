from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse


class Comment(models.Model):
    author = models.ForeignKey(auth.models.User)
    title = models.TextField(max_length=200)
    text = models.TextField(max_length=1024)
    #conference_room =models.ForeignKey('cr_resource.ConferenceRoom',default='Johnson')

    # Allows some of the views to auto send you to the detail view of an object
    def get_absolute_url(self):
        return reverse('comment_detail', args=[str(self.id)])

