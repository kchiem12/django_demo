from django.shortcuts import render
from .models import TodoItem

# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    print(todos)
    return render(request, 'todo_list.html', {'todos': todos})