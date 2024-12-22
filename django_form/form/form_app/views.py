from django.shortcuts import render
from form_app.models import Feedback_logs
from django.http import HttpResponse

# Create your views here.

def show_home(request):
    return render(request,'form_app/templates/index.html')


def record_create_from_backend(request):
    if request.method=='POST':
        v_name=request.POST.get('name')
        v_email=request.POST.get('emails')
        v_message=request.POST.get('message')

        Feedback_logs.objects.create(name=v_name,email=v_email,message=v_message)
        return HttpResponse('Success')
    
    return render(request,'form_app/templates/form.html')
