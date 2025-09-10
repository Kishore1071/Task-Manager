from django.shortcuts import render, redirect
from .models import *
from .forms import *


def task_list(request):

    if request.user.role == 'employee':
        all_tasks = Task.objects.filter(assigned_to=request.user)
    else:
        all_tasks = Task.objects.all()

    context = {
        'all_tasks': all_tasks
    }

    return render(request, 'task_list.html', context)

def create_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'task_add.html', {'form': form, 'button_name': "Create Task"})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_add.html', {'form': form, 'button_name': "Update Task"})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def dashboard(request):
    return render(request, 'dashboard.html', {})










