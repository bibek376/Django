from django.urls import path
from .views import CountryDetail

urlpatterns = [
    path('country/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
]
