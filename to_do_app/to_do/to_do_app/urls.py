from django.contrib import admin
from django.urls import path,include
from to_do_app.views import to_get_all_data,to_add_task,to_check_complete

urlpatterns = [
    path('',to_get_all_data,name="to_do_app"),
    path('add/',to_add_task,name="to_add_task"),
    path('delete/<int:todo_id>',to_check_complete,name="delete_todo"),
]
