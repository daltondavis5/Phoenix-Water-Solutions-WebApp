from rest_framework import serializers
from core.models.utilityprovider import Utility, Location, UtilityProvider, Provider


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['type']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state']


class UtilityProviderSerializer(serializers.ModelSerializer):
    provider_name = serializers.CharField(source='provider.name')
    utility_type = serializers.CharField(source='utility.type')
    city = serializers.CharField(source='location.city')
    state = serializers.CharField(source='location.state')

    class Meta:
        model = UtilityProvider
        fields = ['id', 'provider_name', 'utility_type', 'city', 'state', 'unit_measurement']
        read_only_fields = ['provider_name', 'utility_type', 'city', 'state']

    def create(self, validated_data):
        provider_name = validated_data.get('provider').get('name')
        provider_obj = Provider.objects.get(name=provider_name)

        utility_type = validated_data.get('utility').get('type')
        state = validated_data.get('location').get('state')
        city = validated_data.get('location').get('city')
        utility_obj = Utility.objects.get(type=utility_type)
        location_obj = Location.objects.get(state=state, city=city)
        unit_measurement = float(validated_data.get('unit_measurement'))
        utility_provider = UtilityProvider(
            utility=utility_obj,
            provider=provider_obj,
            location=location_obj,
            unit_measurement=unit_measurement
        )

        utility_provider.save()
        return utility_provider

    def update(self, instance, validated_data):
        instance.unit_measurement = validated_data.get('unit_measurement')
        instance.save()
        return instance


class UtilityProviderSerializer_helper(serializers.ModelSerializer):
    utility_type = serializers.CharField(source='utility.type')
    city = serializers.CharField(source='location.city')
    state = serializers.CharField(source='location.state')

    class Meta:
        model = UtilityProvider
        fields = ['utility_type', 'city', 'state', 'unit_measurement']


class ProviderSerializer(serializers.ModelSerializer):
    utility_provider = UtilityProviderSerializer_helper(
                        source="utilityprovider_set", many=True, read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'name', 'utility_provider']
        read_only_fields = ['utility_provider']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

