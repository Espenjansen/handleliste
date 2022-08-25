from pickle import TRUE
from pickletools import read_uint1
from unicodedata import category, name
from django.shortcuts import render, redirect
from .models import Shoppinglist
from .serializers import ShoppingListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("base/handleliste.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})




# Create your views here.


