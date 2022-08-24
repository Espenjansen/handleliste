from unicodedata import name
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Shoppinglist

class ShoppingListSerializer(ModelSerializer):
    class Meta:
        model = Shoppinglist 
        fields = '__all__' 