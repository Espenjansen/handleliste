from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Item, Shoppinglist
from .forms import CreateNewShoppinglist, NewUserForm, CreateNewItem
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


#ser om du har gjort noe gale under registrering
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        fields = NewUserForm().fields
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("create")

    else:
        form = NewUserForm()
        fields = NewUserForm().fields
    return render(request, "base/register.html", {"form":form, "fields":fields})

#ser om det er noe gale under login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        fields = AuthenticationForm().fields
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("create")

    else:
        form = AuthenticationForm()
        fields = AuthenticationForm().fields
    return render(request, "base/login.html", {'form': form, 'fields': fields})


#lag ny liste
#gjør at form-ene går til en bruker og gjør at bare en kan gå inni dem
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

#hvis request er en post request så lag ein variabel som heter form
#form er ein Item med inputet fra formen på frontend
	if request.method == "POST":
		form = CreateNewItem(request.POST)

#sjekker om det er rett og lagrer det til databasen
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