from pickle import TRUE
from unicodedata import category, name
from django.shortcuts import render
from .models import Shoppinglist
from .serializers import ShoppingListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics

class listShoppingView(generics.ListCreateAPIView):
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppingListSerializer
    def list(self, request):
        #Note the use of get_queryset() instead of self.queryset
        queryset = self.get_queryset()
        serializer = ShoppingListSerializer(queryset, many=True)
        return Response(serializer.data)  


# Create your views here.


