from django.shortcuts import render
from .models import Task

def task_list(request):
    task =Task.object.all()
    return render(request,'task/task_list.html,',{'tasks':tasks})
# Create your views here.
