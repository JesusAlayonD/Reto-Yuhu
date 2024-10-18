from django.urls import path, include
from .views import index, read_tasks, create_tasks, edit_tasks, delete_tasks
from .api import TaskView, TaskUDView

urlpatterns = [
    path('', index, name='index'),
    path('crear_tareas', create_tasks, name='create_tasks'),
    path('ver_tareas', read_tasks, name='read_tasks'),
    path('editar_tareas', edit_tasks, name='edit_tasks'),
    path('eliminar_tareas', delete_tasks, name='delete_tasks'),
    path('api/tasks', TaskView.as_view(), name='tasks'),
    path('api/tasks/<int:id>', TaskUDView.as_view(), name='tasks'),
]