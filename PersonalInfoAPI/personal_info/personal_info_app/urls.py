from django.urls import path
from .views import PersonalInfoList, PersonalInfoDetail

urlpatterns = [
    path('api/v1/personal_info/', PersonalInfoList.as_view(), name='personal_info_list'),  # List and create
    path('api/v1/personal_info/<int:pk>/', PersonalInfoDetail.as_view(), name='personal_info_detail'),  # Retrieve, update, delete by pk
]
