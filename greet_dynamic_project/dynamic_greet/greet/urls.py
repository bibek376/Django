from django.contrib import admin
from django.urls import path,include
from greet.views import dynamic_name_read,home_page_view

urlpatterns = [
    path('greet/<str:d_name>/',dynamic_name_read,name="dynamic_name"),
    path('',home_page_view,name="home_page_url_name"),
]
