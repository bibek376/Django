from django.shortcuts import render

# Create your views here.

#k_name--> Key
#d_name--> dynamic name value

def dynamic_name_read(request,d_name):
    return render(request,'greet/templates/index.html',{'k_name':d_name})


def home_page_view(request):
    return render(request,'greet/templates/home.html')

