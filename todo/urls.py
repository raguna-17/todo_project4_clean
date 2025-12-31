from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/tasks/reorder/', views.TaskReorderView.as_view(), name='task-reorder'),
    path('api/tasks/<int:pk>/', views.TaskDetailAPI.as_view(), name='api-task-detail'),
    path('tasks/', views.TaskListCreateView.as_view(), name='todo-list'),
]


#todo/urls.py