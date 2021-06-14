from .models import *
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"