from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')



# This is the new edit window method
# def editTask(request,pk):
#     get_task = get_object_or_404(Task,pk=pk)
#     print(get_task)
#     if request.method == 'POST':
#         new_task = request.POST['task']
#         get_task.task = new_task
#         get_task.save()
#         return redirect('home')
#     else:
#         context = {
#             'get_task' : get_task,
#         }
#         return render(request,'edit_task.html',context)



# This is the pop-up edit method
def editTask(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_task = request.POST.get('task')

        get_task = get_object_or_404(Task, pk=task_id)
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    # else:
    #     get_task = get_object_or_404(Task, pk=pk)
    #     context = {
    #         'get_task': get_task,
    #     }
    #     return render(request, 'home.html', context)
    
def deleteTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')