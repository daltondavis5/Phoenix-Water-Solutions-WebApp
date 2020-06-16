from rest_framework import serializers
from core.models.utilityprovider import *


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['utility_type']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state']


class UtilityProviderSerializer(serializers.ModelSerializer):
    utility = UtilitySerializer()
    location = LocationSerializer()

    class Meta:
        model = UtilityProvider
        fields = ['utility', 'location', 'unit_measurement']


class ProviderSerializer(serializers.ModelSerializer):
    utility_provider = UtilityProviderSerializer(
        source="utilityprovider_set", many=True)

    class Meta:
        model = Provider
        fields = ['name', 'utility_provider']

    def create(self, validated_data):
        # print("Data: ", validated_data)
        utility_provider_data = validated_data.pop('utilityprovider_set')
        provider = Provider.objects.create(**validated_data)

        for utility in utility_provider_data:
            utility_type = utility.get('utility').get('utility_type')
            state = utility.get('location').get('state')
            city = utility.get('location').get('city')
            utility_obj = Utility.objects.get(utility_type=utility_type)
            location_obj = Location.objects.get(
                state=state, city=city)
            utility_provider = UtilityProvider(
                utility=utility_obj,
                provider=provider,
                location=location_obj,
                unit_measurement=float(
                    utility['unit_measurement'])
            )
            utility_provider.save()

        return provider
