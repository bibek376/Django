from rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    def validate(self, data):
        """
        Ensure email belongs to the username provided.
        """
        from django.contrib.auth.models import User

        username = data.get('username')
        email = data.get('email')

        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or email combination.")
        return data


