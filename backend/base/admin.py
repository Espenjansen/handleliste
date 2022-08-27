from django.contrib import admin
from .models import Item, Shoppinglist


# Register your models here.
admin.site.register(Shoppinglist)
admin.site.register(Item)