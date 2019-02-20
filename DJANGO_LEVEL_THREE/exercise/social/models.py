from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=254)
    lname = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return fname
