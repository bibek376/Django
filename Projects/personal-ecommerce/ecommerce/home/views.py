from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

# def home(request):
#     return render(request,'index.html')



#class based view

class BaseView(View):
    Views={}    

class HomeView(BaseView):

    def get(self,request):
        self.Views['items']=Item.objects.filter(offer=True)
        self.Views['sliders']=Slider.objects.all()
        self.Views['hot_items']=Item.objects.filter(labels='hot')
        self.Views['sale_items']=Item.objects.filter(labels='sale')
        self.Views['new_items']=Item.objects.filter(labels='new')
        self.Views['ads']=Ad.objects.all()
        self.Views['categories']=Category.objects.all()
        self.Views['subcategories']=SubCategory.objects.all()

        return render(self.request,'index.html',self.Views)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.Views['products']=Item.objects.filter(slag=slug)
        return render(self.request,'products.html',self.Views)

class SearchView(BaseView):
    def get(self,request):
        query=request.GET.get('query',None)
        if not query:
            return redirect('/')
        self.Views['search_query'] = Item.objects.filter(title__icontains = query)
        return render(request,'search.html',self.Views)
 

class SubCategoryView(BaseView):
     def get(self,request,slug):
         ids=SubCategory.objects.get(slug=slug).id
         self.Views['subcat_products'] = Item.objects.filter(subcategory_id=ids)
         return render(request,'subcategory.html',self.Views)
 

def signup(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']
        cpassword=request.POST['CPassword']
        if password == cpassword:
             if User.objects.filter(username=username).exists():
                messages.error(request,'The user name is already taken')
                return redirect('/signup')

             if User.objects.filter(email=email).exists():
                messages.error(request,'Email is Not Available')
                return redirect('/signup')

             else:
                 user=User.objects.create_user(
                     username=username,
                     email=email,
                     password=password
                 )
                 user.save()
                 messages.error(request,'You are registered')
                 return redirect('/')

    else:
        messages.error(request,'The password does not match')
        return redirect('/signup')

            

    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'There is some error')
            return redirect('home:login')
    return render(request,'login.html')


def add_to_cart(request,slug):
    user=request.user.username
    if Cart.objects.filter(slug=slug,user=user).exists():
        quantity=Cart.objects.get(slug=slug).quantity
        quantity=quantity + 1
        Cart.objects.filter(slug=slug).update(quantity=quantity)
        messages.success(request,"The quantity is updated.")
        return redirect('/')
    else:
        products=Cart.objects.create(
            user=user,
            product=Item.objects.filter(slug=slug)[0],#here
            slug=slug
        )
        products.save()
        messages.success(request,"The item is added")
        return redirect('/')


class CartView(BaseView):
    def get(self,request):
        self.Views['my_carts']=Cart.objects.filter(user=request.user,checkout=True)
        return render(self.request,'cart.html',self.Views)



#API Section
from home.serializers import *
from rest_framework import Viewsets

class ItemViewSet(Viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializers