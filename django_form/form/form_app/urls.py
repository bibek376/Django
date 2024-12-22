from django.contrib import admin
from django.urls import path,include
from form_app.views import show_home,record_create_from_backend


urlpatterns = [
    path('',show_home,name='landing_page'),
    path('form/',record_create_from_backend,name='form_submission'),
]
