from django.db import models
from django.contrib.auth.models import User

TYPES = [
    ("coupe", "Coupe"),
    ("sedan", "Sedan"),
    ("hatchback", "Hatch Back"),
    ("suv", "SUV"),
    ("sports", "Sports"),
]

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

    class Meta:
        ordering = ['name']


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    description = models.TextField()
    release_date = models.DateField()
    body_type = models.CharField(choices=TYPES, default="sedan", max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __str__(self):
    	return self.name

    class Meta:
        ordering = ['name']

class Ownership(models.Model):
    reg_no = models.CharField(max_length=40, default="KL-01-ABC-1234", unique=True)
    purchase_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)

    def __str__(self):
        return self.reg_no

    class Meta:
        ordering = ['reg_no']