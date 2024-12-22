from django.contrib import admin
from django.urls import path
from crud_app.views import home,create_view,success_view,to_list_all,detailed_data

urlpatterns = [
    path('',home,name="landing_page"),
    path('form/',create_view,name="create_view"),
    path('success/',success_view,name="success_page"),
    path('all/',to_list_all,name="all_data"),
    path('all/<int:pk>/',detailed_data,name="detailed_data"),
]
