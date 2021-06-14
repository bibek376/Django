from django.shortcuts import render
from django.views.generic import View
from .models import Item,Ad,Category,SubCategory

# Create your views here.

# def home(request):
#     return render(request,'index.html')



#class based view

class BaseView(View):
    views={}

class HomeView(BaseView):

    def get(self,request):

        self.views['items']=Item.objects.all()
        self.views['ads']=Ad.objects.all()
        self.views['categories']=Category.objects.all()
        self.views['subcategories']=SubCategory.objects.all()

        return render(self.request,'index.html',self.views)
