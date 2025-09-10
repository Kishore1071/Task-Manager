from django.urls import path
from .views import *

urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('create/', create_task, name='task_create'),
    path('update/<int:task_id>/', update_task, name='task_update'),
    path('delete/<int:task_id>/', delete_task, name='task_delete'),

    path('dashboard/', dashboard, name='dashboard'),
]