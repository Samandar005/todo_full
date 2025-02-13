from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo-list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        todos = Todo.objects.all()
        status = self.request.GET.get('status')
        search_query = self.request.GET.get('search')
        priority = self.request.GET.get('priority')
        order_by = self.request.GET.get('order_by')

        if status:
            todos = todos.filter(completed=(status == 'completed'))
        if search_query:
            todos = todos.filter(title__icontains=search_query)
        if priority:
            todos = todos.filter(priority=priority)
        if order_by == 'date':
            todos = todos.order_by('created_at')
        elif order_by == 'priority':
            todos = todos.order_by('priority')
        elif order_by == 'status':
            todos = todos.order_by('completed')
        return todos

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    context_object_name = 'todo'

    def get_object(self, queryset=None):
        return get_object_or_404(Todo, slug=self.kwargs.get('slug'))

class CreateTodoView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/form.html'
    success_url = reverse_lazy('todo:list')

class UpdateTodoView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/form.html'
    context_object_name = 'todo'

    def get_success_url(self):
        return self.object.get_detail_url()

class DeleteTodoView(DeleteView):
    model = Todo
    template_name = 'todo/confirm.html'
    success_url = reverse_lazy('todo:list')

class TodoStatusView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return redirect('todo:list')