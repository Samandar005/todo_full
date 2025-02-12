from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, View
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo-list.html'
    context_object_name = 'todos'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    context_object_name = 'todo'

class CreateTodoView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/form.html'
    success_url = reverse_lazy('todo:list')

class UpdateTodoView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/form.html'
    success_url = reverse_lazy('todo:list')
    context_object_name = 'todo'

class DeleteTodoView(DeleteView):
    model = Todo
    template_name = 'todo/confirm.html'
    success_url = reverse_lazy('todo:list')
