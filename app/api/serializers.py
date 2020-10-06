from rest_framework import serializers

from api.models import Manufacturer, Car, Ownership, Owner


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='car-detail')

    class Meta:
        model = Manufacturer
        fields = ['url', 'name', 'about', 'location', 'cars']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    ownerships = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ownership-detail')

    class Meta:
        model = Car
        fields = ['url', 'name', 'price', 'description', 'release_date', 'body_type', 'manufacturer', 'ownerships']


class OwnershipSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ownership
        fields = ['url', 'reg_no', 'purchase_date', 'owner', 'car']


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    ownerships = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='ownership-detail')

    class Meta:
        model = Owner
        fields = ['url', 'fullname', 'username', 'email', 'bio', 'location', 'birth_date', 'is_staff', 'ownerships']
