from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django import forms
from comment.models import Comment

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(
        queryset=User.objects.all())
    text = forms.CharField(
        label="Comment",
        max_length=1024,
        widget=forms.Textarea)

class CommentList(ListView):
    model = Comment

    # adding a form to a listview
    def get_context_data(self, **kwargs):
        form = CommentForm
        context = super(CommentList, self).get_context_data(**kwargs)
        context['form'] = form
        return context

class CommentDetail(DetailView):
    model = Comment

class CommentCreate(CreateView):
    model = Comment
    fields = ['author', 'text']

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['author', 'title', 'text']

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_list')