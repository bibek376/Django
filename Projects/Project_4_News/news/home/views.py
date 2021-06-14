from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from .models import *
import datetime
# Create your views here.

class BaseView(View):
    views={}

class Home(BaseView):

    def get(self,request):
        self.views['navbar']=Nav.objects.all()
        self.views['picture']=Picture.objects.all()
        self.views['newsproduct']=NewsProduct.objects.filter(labels='weeklytop')
        # date=datetime.datetime.now()
        # date=date.strftime("%c")
        # mydict={'saj':date}


        return render(self.request,'index.html',self.views)


def Myfunc(request):
     date=datetime.datetime.now()
     date=date.strftime("%c")
     mydict={'saj':date}


     return render(request,'index.html',context=mydict)




class ContactView(BaseView):

    def get(self,request):
        if request.method == 'POST':
            name=request.POST['name']
            email=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']

            data=Contact.objects.create(name=name,email=email,subject=subject,message=message)
            # (name,name)=(databasefield,object)
            data.save()
            # return reverse('/')

        return render(self.request,'contact.html',self.views)

class More(BaseView):
    def get(self,request):

        return render(self.request,'details.html',self.views)



def search(request):
    post=NewsProduct.objects.all()
    para={'post':post}



    # return HttpResponse('This is search')
