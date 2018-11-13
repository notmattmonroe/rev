from luke.todolist.models import Todo
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Todo.objects.all()
    return render_to_response('todolist/index.html', {'items':items})