from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.


def home_view(request):
    return render(request,'login_app/templates/home.html')


def login_page(request):
    if request.method=='POST':
        v_email=request.POST.get('email')
        v_password=request.POST.get('password')
        print(v_email,v_password)
        user_auth=authenticate(request,email=v_email,password=v_password)
        if user_auth is not None:
            signup_page(request,user_auth)
            return redirect('home_page')
        else:
            return HttpResponse("password or username did not matched...")
    return render(request,'login_app/templates/login.html')


def signup_page(request):
    if request.method=='POST':
        v_name=request.POST.get('name')
        v_email=request.POST.get('email')
        v_password1=request.POST.get('password1')
        v_password2=request.POST.get('password2')
        print(v_name,v_email,v_password1,v_password2)
        if v_password1!=v_password2:
            return HttpResponse("Password Did not matched ?")
        else:
            new_user=User.objects.create_user(v_name,v_email,v_password1)
            new_user.save()
            return redirect('login_up_page')
    return render(request,'login_app/templates/signup.html')