from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shoppinglist(models.Model):
    name = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    shoppinglist = models.ForeignKey(Shoppinglist, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
