from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User, Task
from .forms import *
from django.shortcuts import redirect, get_object_or_404


def home(request):
    loginform = loginForm()
    return render(request, 'home.html', {'loginform':loginform})



def index(request):
    username = request.session['user']
    tasks = Task.objects.filter(user=username)
    return render(request, 'index.html', {'tasks':tasks})


def login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['passwod']
        try:
            x = User.objects.get(email=username,passwod=password)
        except:
            x=None
        if x:
            request.session['user'] = x.userId
            return redirect('index')
        else:
            return HttpResponse("wrong")
    else:
        form = loginForm()
    return render(request, 'home.html', {'form': form})


def addnew(request):
    form = TaskForm()
    return render(request, 'addnew.html', {'form': form})


def saveAddNew(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = User.objects.get(userId=request.session['user'])
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'addnew.html', {'form': form})


def editPost(request, pk):
    post = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = TaskForm(instance=post)
    return render(request, 'editPost.html', {'form': form})


def deletePost(request, pk):
    post = get_object_or_404(Task, pk=pk)
    post.delete()
    return redirect('index')