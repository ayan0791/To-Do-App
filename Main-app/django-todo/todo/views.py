from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            Todo.objects.create(title=title)

        return redirect('index')

    todos = Todo.objects.all()

    return render(request, 'todo/index.html', {'todos': todos})


def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('index')

    return render(request, 'todo/edit.html', {'todo': todo})

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

    return render(request, 'todo/edit.html', {'todo': todo})


def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    todo.completed = True
    todo.save()

    return redirect('index')

def clear_all(request):
    Todo.objects.all().delete()
    return redirect('index')




# Create your views here.
