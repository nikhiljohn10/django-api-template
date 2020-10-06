from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

TYPES = [
    ("coupe", "Coupe"),
    ("sedan", "Sedan"),
    ("hatchback", "Hatch Back"),
    ("suv", "SUV"),
]

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
    	return self.name

    class Meta:
        ordering = ['name']


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    body_type = models.CharField(choices=TYPES, default="sedan", max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, related_name='cars', on_delete=models.PROTECT)

    def __str__(self):
    	return self.name

    class Meta:
        ordering = ['name']

class Ownership(models.Model):
    reg_no = models.CharField(max_length=40, default="KL-01-ABC-1234", unique=True)
    purchase_date = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ownerships', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='ownerships', on_delete=models.RESTRICT)

    def __str__(self):
        return self.reg_no

    class Meta:
        ordering = ['reg_no']

class Owner(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cash = models.DecimalField(max_digits=20, decimal_places=2, default=1000000)

    @property
    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
