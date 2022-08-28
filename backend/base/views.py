from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Item, Shoppinglist
from .forms import CreateNewShoppinglist, NewUserForm, CreateNewItem
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
			return redirect("create")
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
				return redirect("create")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})


def index(request):
    return render(request,"base/index.html",{})





#lag ny liste
#gjøre at brukere må logge inn får å gjøre noe
def create_list(request):
	if request.method == "POST":
		form = CreateNewShoppinglist(request.POST)

		if form.is_valid():
			u = request.user
			n = form.cleaned_data["name"]
			s = Shoppinglist(name=n)
			s.save()
			request.user.shoppinglist.add(s)

		return HttpResponseRedirect("/%i" %s.id)
	else:
		form = CreateNewItem()
	list = Shoppinglist.objects.all()
	context = {
		"list":list,
		"form":form
	}
	return render(request, "base/create.html", context)


#side med individuelle lister
def shoppingdetail(request, id):
	ls = Shoppinglist.objects.get(id=id)

	if request.method == "POST":
		form = CreateNewItem(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			i = Item(name=n, shoppinglist=ls)
			i.save()
	else:
		form = CreateNewItem()
	items=ls.get_Items()
	context = {
		"items":items,
		"ls": ls,
		"form": form
	}
	return render(request, "base/detail.html", context)
	
def view(request):
	return render(request, "base/view.html", {})