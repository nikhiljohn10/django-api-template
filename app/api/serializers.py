from rest_framework import serializers

from django.contrib.auth.models import  User
from api.models import Car, Manufacturer, Ownership

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['url', 'name', 'price', 'description', 'release_date', 'body_type', 'manufacturer']


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['url', 'name',]



class OwnershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ownership
        fields = ['url', 'reg_no', 'purchase_date', 'owner', 'car']
        
    def create(self, validated_data):
        return Ownership.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.reg_no = validated_data.get('reg_no', instance.reg_no)
        instance.purchase_date = validated_data.get('purchase_date', instance.purchase_date)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.car = validated_data.get('car', instance.car)
        instance.save()
        return instance