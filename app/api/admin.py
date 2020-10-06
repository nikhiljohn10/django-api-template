from django.contrib import admin
from django.contrib.auth.models import Group

from api.models import Manufacturer, Car, Ownership, Owner

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(Owner)

admin.site.unregister(Group)
