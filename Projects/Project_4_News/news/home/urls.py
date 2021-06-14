from django.urls import path
from .views import *


app_name='home'

urlpatterns = [
    path('',Home.as_view(), name="index"),
    path('contact/',ContactView.as_view(), name="contact"),
    path('details/',More.as_view(), name="more"),
    path('',Myfunc,name="myfunc"),
    path('search',search,name='search'),
]
