from django.shortcuts import render
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Tag


class TagBaseForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'tagid', 'volume', 'uri','source']

class TagCreate(CreateView):
    model = Tag
    form_class = TagBaseForm

class TagUpdate(UpdateView):
    model = Tag
    form_class = TagBaseForm

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')

class TagList(ListView):
    model = Tag
