from django.urls import path
from .views import *

app_name='home'

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('products/<slug>',ProductDetailView.as_view(),name="products"),
    path('subcat/<slug>',SubCategoryView.as_view(),name="subcat"),
    path('search/',SearchView.as_view(),name="search"),
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('add-to-cart/<slug>',add_to_cart,name="add-to-cart"),
    path('mycart/',CartView.as_view(),name="mycart"),
]
