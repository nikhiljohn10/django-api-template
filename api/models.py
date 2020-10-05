from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField()
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
