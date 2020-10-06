from rest_framework import viewsets

from api.serializers import ManufacturerSerializer, CarSerializer, OwnershipSerializer, OwnerSerializer
from api.models import Manufacturer, Car, Ownership, Owner

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class OwnershipViewSet(viewsets.ModelViewSet):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
