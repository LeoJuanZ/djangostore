from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    email = models.EmailField()
    tlf = models.CharField(max_length=7)

class Items(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price = models.IntegerField()

class CashOrder(models.Model):
    number =  models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()

