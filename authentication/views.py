from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout

def sample_view(request):
    return render(request, 'sample.html', {})

def user_list(request):
    all_users = User.objects.all()

    context = {
        'all_users': all_users
    }

    return render(request, 'user_list.html', context)

def create_user(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('user_list')
    else:
        form = UserForm()
    
    return render(request, 'user_add.html', {'form': form, 'button_name': "Create User"})

def update_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'user_add.html', {'form': form, 'button_name': "Update User"})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')
