from rest_framework import serializers
from .models import Employee,MbDfsTrans,Country

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class MbDfsTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = MbDfsTrans
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

