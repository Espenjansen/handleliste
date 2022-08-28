from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shoppinglist(models.Model):
        
    def get_Items(self):
        return Item.objects.filter(shoppinglist=self.id)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shoppinglist", null=True)
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    shoppinglist = models.ForeignKey(Shoppinglist, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


