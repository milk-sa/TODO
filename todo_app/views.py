from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect



def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'todo_app/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        
        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')
    return render(request, 'todo_app/add.html')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return redirect('task_list')  # fallback in case someone accesses via GET

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('task_list')

    return render(request, 'todo_app/edit.html', {'task': task})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('task_list')
