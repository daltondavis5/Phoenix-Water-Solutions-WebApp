from rest_framework import serializers
from core.models.utilityprovider import *


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['utility_type']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state']


class UtilityProviderSerializer(serializers.ModelSerializer):
    utility = UtilitySerializer()
    provider = ProviderSerializer()
    location = LocationSerializer()

    class Meta:
        model = UtilityProvider
        fields = ['id', 'utility', 'provider', 'location', 'unit_measurement']
        depth = 1


"""     def create(self, validated_data):
        print(validated_data)
        provider = Provider(name=validated_data['provider']['name'])
        provider.save()
        return provider """
