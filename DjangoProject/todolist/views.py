from django.shortcuts import render
from django.views import View, generic

from todolist.models import todo


# Create your views here.
class TodoListView(generic.ListView):
    model = todo
    template_name = 'list.html'
class TodoCreateView(generic.CreateView):
    model = todo
    template_name = 'create.html'
    fields = ['title','description','is_active']
class TodoUpdateView(generic.UpdateView):
    model = todo
    template_name = 'update.html'
class TodoDeleteView(generic.DeleteView):
    model = todo
    template_name = 'delete.html'
