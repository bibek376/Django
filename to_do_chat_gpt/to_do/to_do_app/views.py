from django.shortcuts import render,redirect,get_object_or_404
from to_do_app.models import TodoItem
from to_do_app.forms import TodoItemForm
# Create your views here.

def list_view(request):
    todos = TodoItem.objects.all()
    return render(request,'to_do_app/templates/todo_list.html',{'forms':todos})


def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'to_do_app/templates/todo_form.html', {'form': form})


def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk)
    
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    
    return render(request, 'to_do_app/templates/todo_confirm_delete.html', {'todo': todo})


def update_todo(request, pk):
    todo = get_object_or_404(TodoItem, id=pk)
    
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    
    return render(request, 'to_do_app/templates/todo_form.html', {'form': form, 'action': 'Update'})
