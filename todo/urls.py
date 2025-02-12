from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('create/', views.CreateTodoView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateTodoView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete'),
    path('status/<int:pk>/', views.TodoStatusView.as_view(), name='status'),
]