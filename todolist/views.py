from datetime import date, datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from todolist.models import Task, TaskCount
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
            response = HttpResponseRedirect(reverse("todolist:ajax")) # create response
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
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

@login_required(login_url='/todolist/login/')
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

    context = {'form':form, 'name':request.user.get_username(), 'date':datetime.now().strftime('%x')}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def finished_status(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def todolist_json(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    data = Task.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {
        'name': user.get_username(),
        'date': datetime.now().strftime('%x'),
        'count': Task.objects.filter(user=request.user).count(),
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/')
def update_ajax(request, id):
    task = get_object_or_404(Task, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def delete_ajax(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return HttpResponseNotFound()

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_task = Task(user=request.user, title=title, description=description)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()