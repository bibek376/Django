from django.shortcuts import render,redirect
from to_do_app.models import my_task
# Create your views here.


def to_get_all_data(request):
    all_data=my_task.objects.all()
    return render(request,'to_do_app/templates/index.html',{'v_all_data':all_data})


def to_add_task(request):
    if request.method=="post":
        v_task_name=request.POST.get('task_name')
        v_is_complete=request.POST.get('is_complete')

        to_do=my_task.objects.create(task_name=v_task_name,is_complete=v_is_complete)
        to_do.save()

        return redirect('to_do_app/templates/index.html') 


def to_check_complete(request,todo_id):
    to_delete=my_task.objects.get(id=todo_id)
    to_delete.delete()

    return redirect('to_do_app/templates/index.html')

