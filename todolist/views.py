import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from todolist.models import Task
from todolist.forms import CreateTask

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    data_todolist_item = Task.objects.filter(user=user)
    context = {
        'list_item': data_todolist_item,
        'name': user.get_username(),
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    form = CreateTask()
    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            form.save()
            messages.success(request, 'New task successfully created!')
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)

def finished_status(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))