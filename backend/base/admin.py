from django.contrib import admin
from .models import Item, Shoppinglist, Note


# Register your models here.
admin.site.register(Shoppinglist)
admin.site.register(Item)
admin.site.register(Note)