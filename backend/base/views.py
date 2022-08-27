from re import I
from django.shortcuts import render, redirect
from .models import Shoppinglist
from .forms import NewUserForm, CreateNewItem
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

#lag views her:

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})


def index(request):
    return render(request,"base/index.html",{})

def list(request):
	list = Shoppinglist.objects.all()
	return render(request, "base/list.html", {"list":list})

def create(request):
	if request.method == "POST":
		form = CreateNewItem(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			i = Shoppinglist(name=n)
			i.save()
	else:
		form = CreateNewItem()
	return render(request, "base/create.html", {"form":form})