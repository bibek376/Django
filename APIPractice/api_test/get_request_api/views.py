from django.shortcuts import render
from rest_framework import generics
from .models import Employee,MbDfsTrans,Country
from .serializers import EmployeeSerializer,MbDfsTransSerializer,CountrySerializer


from django.http import JsonResponse
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MbDfsTransListCreateView(generics.ListCreateAPIView):
    queryset = MbDfsTrans.objects.all()
    serializer_class = MbDfsTransSerializer

class MbDfsTransDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MbDfsTrans.objects.all()
    serializer_class = MbDfsTransSerializer

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class EmployeeCountryReportView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT e.name, c.country_name
                FROM public.employee e
                INNER JOIN public.country c
                ON e.country_id = c.id;
            ''')
            rows = cursor.fetchall()  # Fetch all rows from the query result

        # Prepare the data to be returned in JSON format
        result = []
        for row in rows:
            result.append({
                'employee_name': row[0],
                'country_name': row[1]
            })
        
        return Response(result, status=status.HTTP_200_OK)
