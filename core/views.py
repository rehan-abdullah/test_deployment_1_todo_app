from django.shortcuts import render
from todos.models import Todo


def home_page(request):

    todos = Todo.objects.all()

    context = {
        'todos_list': todos,
    }

    return render(request, "index.html", context)
