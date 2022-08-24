import imp
from unicodedata import category, name
from django.shortcuts import render
from backend.base import serializers
from models import Shoppinglist
from serializers import ShoppingListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class listShoppingView(APIView):
    serializers_class = ShoppingListSerializer
    def get(self, request, format=None):
        names = [Shoppinglist.name for Shoppinglist in Shoppinglist.object.all()]
        return Response(name)
# Create your views here.


