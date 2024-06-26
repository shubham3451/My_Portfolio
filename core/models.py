from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=250)
    message = models.CharField( max_length=5000)
