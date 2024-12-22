from django.urls import path
from .views import LoginAPIView,UserRegistrationAPIView

urlpatterns = [
    path('auth/register/', UserRegistrationAPIView.as_view(), name='auth_user_create'),
    path('auth/login/', LoginAPIView.as_view(), name='auth_login'),
]


