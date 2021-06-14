from django.shortcuts import render

from .models import *

# Create your views here.


def homeview(request):
    views={}
    views['feedbacks']=FeedBack.objects.all()
    return render(request,'index.html',views)



def aboutview(request):
    return render(request,'about.html')



def contactview(request):
    #for feedbasck in a contact file....
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        #object relational mapping...

        data=contact(name=name,email=email,subject=subject,message=message)
        data.save()




    return render(request,'contact.html')



def portfolioview(request):
    return render(request,'portfolio.html')


def priceview(request):
    return render(request,'price.html')


def servicesview(request):
    return render(request,'services.html')
