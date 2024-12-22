from django.contrib import admin
from django.urls import path
from emp_app.views import emp_list,emp_update_insert,emp_delete,edit_employee

urlpatterns = [
    path('',emp_list,name="emp_list"),
    path('add/',emp_update_insert,name="employee_insert_update"),
    path('delete/<int:pk>',emp_delete,name="delete_employee"),
    path('edit/<int:pk>',edit_employee,name="edit_employee"),
]


