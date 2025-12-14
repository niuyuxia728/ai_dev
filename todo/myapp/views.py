from django.shortcuts import render, redirect
from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


def todo_list(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_list.html', {'form': form, 'todos': todos})


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('todo_list')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
