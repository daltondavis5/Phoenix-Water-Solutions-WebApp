from rest_framework import serializers
from core.models.utilityprovider import Utility, Location, \
    UtilityProvider, Provider


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
        # fields = ['id', 'provider_name', 'utility_type', 'city',
        #           'state', 'unit_measurement']
        # read_only_fields = ['provider_name', 'utility_type', 'city', 'state']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['provider_name', 'utility_type', 'city', 'state'],
            )
        ]
        fields = ['id', 'provider_name', 'utility_type', 'city',
                  'state', 'unit_measurement']

    def validate(self, data):
        print("In validate", data)
        instance = self.instance

        provider_name = data.get('provider').get('name')
        utility_type = data.get('utility').get('type')
        state = data.get('location').get('state')
        city = data.get('location').get('city')

        # if utility_provider objects exists in db (Update)
        if instance is not None:
            if instance.provider.name != provider_name:
                raise serializers.ValidationError("Not allowed to change"
                                                  " provider name. ")

            if instance.utility.type != utility_type:
                raise serializers.ValidationError("Not allowed to change"
                                                  " utility type of provider")

            if instance.location.city != city:
                raise serializers.ValidationError("Not allowed to change "
                                                  "provider city. ")

            if instance.location.state != state:
                raise serializers.ValidationError("Not allowed to change "
                                                  "provider state. ")
            return data

        # if utility_provider does not exist (Create)
        else:
            if not Provider.objects.filter(name=provider_name).exists():
                raise serializers.ValidationError("No provider found in "
                                                  "database. ")

            if not Utility.objects.filter(type=utility_type).exists():
                raise serializers.ValidationError("No utility found in "
                                                  "database. ")

            if not Location.objects.filter(state=state, city=city).exists():
                raise serializers.ValidationError("No location found in "
                                                  "database. ")
            return data

    def create(self, validated_data):
        provider_name = validated_data.get('provider').get('name')
        utility_type = validated_data.get('utility').get('type')
        state = validated_data.get('location').get('state')
        city = validated_data.get('location').get('city')

        provider_obj = Provider.objects.get(name=provider_name)
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


class ProviderSerializer(serializers.ModelSerializer):
    utility_provider = UtilityProviderSerializer(
        source="utilityprovider_set", many=True,
        read_only=True)

    class Meta:
        model = Provider
        fields = ['id', 'name', 'utility_provider']
        read_only_fields = ['utility_provider']
