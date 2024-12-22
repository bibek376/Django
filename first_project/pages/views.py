from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    random_num=random.randint(1,10)
    context={
        'random': random_num
    }
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html')
