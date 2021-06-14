from . import views
from django.urls import path

# app_name='home'

urlpatterns=[
    path('',views.homeview,name="home"),
    path('about',views.aboutview,name="about"),
    path('contact',views.contactview,name="contact"),
    path('portfolio',views.portfolioview,name="portfolio"),
    path('price',views.priceview,name="price"),
    path('services',views.servicesview,name="services"),
]