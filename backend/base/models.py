from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Shoppinglist(models.Model):
    name = models.CharField(max_length = 255)