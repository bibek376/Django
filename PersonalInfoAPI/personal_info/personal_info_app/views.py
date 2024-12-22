from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer
import requests


def validate_phone_number(phone_number):
    """
    Validates a phone number to ensure it is exactly 10 digits and non-negative.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        tuple: (is_valid (bool), error_message (str or None))
    """
    if phone_number is None:
        return True, None  # No validation needed if phone_number is not provided
    
    if not phone_number.isdigit() or len(phone_number) != 10 or int(phone_number) < 0:
        return False, 'The phone number must be exactly 10 digits and non-negative.'
    
    return True, None


class PersonalInfoList(APIView):
    def get(self, request):
        personal_infos = PersonalInfo.objects.all()  # Fetch all records from the PersonalInfo model
        serializer = PersonalInfoSerializer(personal_infos, many=True)  # Serialize the records
        return Response(serializer.data)  # Return the serialized data as a JSON response

    def post(self, request):

        phone_number = request.data.get("phone")
        
        is_valid, error_message = validate_phone_number(phone_number)
        if not is_valid:
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonalInfoSerializer(data=request.data)  # Deserialize the incoming data

        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the new record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created record with a 201 status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if data is invalid

class PersonalInfoDetail(APIView):

    def get(self, request, pk):
        try:
            personal_info = PersonalInfo.objects.get(pk=pk)  # Retrieve the record with the provided primary key
        except PersonalInfo.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)  # Return a 404 if not found

        serializer = PersonalInfoSerializer(personal_info)  # Serialize the found record
        return Response(serializer.data)  # Return the serialized data as a JSON response
    
    def put(self, request, pk):
        try:
            personal_info = PersonalInfo.objects.get(pk=pk)  # Retrieve the record for updating
        except PersonalInfo.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)  # Return a 404 if not found
    
        phone_number = request.data.get("phone")
        
        is_valid, error_message = validate_phone_number(phone_number)
        if not is_valid:
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonalInfoSerializer(personal_info, data=request.data)  # Deserialize the incoming update data

        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save the updated record
            return Response(serializer.data)  # Return the updated record
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors if data is invalid

    def delete(self, request, pk):
        try:
            personal_info = PersonalInfo.objects.get(pk=pk)  # Retrieve the record to delete
        except PersonalInfo.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)  # Return a 404 if not found

        personal_info.delete()  # Delete the record
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)  # Return a success message

    def patch(self, request, pk):
        try:
            personal_info = PersonalInfo.objects.get(pk=pk)
        except PersonalInfo.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        phone_number = request.data.get("phone")
        
        print("Phone number is:",phone_number)

        is_valid, error_message = validate_phone_number(phone_number)
        if not is_valid:
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = PersonalInfoSerializer(personal_info, data=request.data, partial=True)  # Allow partial updates

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

