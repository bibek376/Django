# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import Countries  
# from .serializers import CountriesSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class CountryDetail(APIView):
    def get(self, request, pk):
        try:
            country = Countries.objects.get(pk=pk)
            data = {
                "id": country.id,
                "name": country.name,
                "code": country.code,
            }
            return Response(data)  # Use DRF's Response object
        except Countries.DoesNotExist:
            return Response({"error": "Country not found"}, status=404)
