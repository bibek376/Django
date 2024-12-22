from django.urls import path
from login_app.views import login_page,signup_page,home_view

urlpatterns = [
    path('',login_page,name="login_up_page"),
    path('signup/',signup_page,name="sign_up_page"),
    path('home/',home_view,name="home")
]




