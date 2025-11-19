from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.db.models import Q


def home(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=False)
    return render(request, 'home.html', {'tasks': tasks})



def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            is_deleted=False
        )
        return redirect('home')

    return render(request, 'add.html')



def update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('home')

    return render(request, 'update.html', {'task': task})



def delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_deleted = True
    task.save()
    return redirect('home')



def trash(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=True)
    return render(request, 'trash.html', {'tasks': tasks})



def delete_permanent(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('trash')



def restore(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_deleted = False
    task.save()
    return redirect('trash')



def restore_all(request):
    Task.objects.filter(user=request.user, is_deleted=True).update(is_deleted=False)
    return redirect('trash')



def clear_all(request):
    Task.objects.filter(user=request.user, is_deleted=True).delete()
    return redirect('trash')
