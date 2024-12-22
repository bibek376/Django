from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView,MbDfsTransListCreateView,MbDfsTransDetailView,CountryListCreateView,CountryDetailView,EmployeeCountryReportView

urlpatterns = [
    path('api/v1/employee/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/v1/employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('api/v1/item/', MbDfsTransListCreateView.as_view(), name='MbDfsTrans-list-create'),
    path('api/v1/item/<int:pk>/', MbDfsTransDetailView.as_view(), name='MbDfsTrans-detail'),
    path('api/v1/country/', CountryListCreateView.as_view(), name='country-list-create'),
    path('api/v1/country/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('api/v1/report/', EmployeeCountryReportView.as_view(), name='employee-country-report'),
]
