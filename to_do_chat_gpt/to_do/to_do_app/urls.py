from django.urls import path
from to_do_app.views import list_view,add_todo,update_todo,delete_todo

urlpatterns = [
    path('',list_view,name="todo_list"),
    path('add/',add_todo,name="add_todo"),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
]


