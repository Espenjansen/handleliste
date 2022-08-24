from unicodedata import name
from rest_framework import serializers

class ShoppingListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    