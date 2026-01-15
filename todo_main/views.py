from django.shortcuts import render
from datetime import date
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    c_tasks = Task.objects.filter(is_completed=True)
    context = {
        "tasks": tasks,
        "c_tasks": c_tasks,
        "today": date.today()
    }
    return render(request, "home.html",context)
