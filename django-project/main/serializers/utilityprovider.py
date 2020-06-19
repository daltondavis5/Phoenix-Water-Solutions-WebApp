from rest_framework import serializers
from core.models.utilityprovider import Utility, Location, UtilityProvider, Provider


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['utility_type']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state']


class UtilityProviderSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name')
    utility_type = serializers.CharField(source='utility.utility_type')
    city = serializers.CharField(source='location.city')
    state = serializers.CharField(source='location.state')

    class Meta:
        model = UtilityProvider
        fields = ['provider', 'utility_type', 'city', 'state', 'unit_measurement']

    def create(self, validated_data):
        print("in UtilityProviderSerializer create")
        print(validated_data)

        provider_name = validated_data.get('provider').get('name')
        provider_obj = Provider.objects.get(name=provider_name)
        provider_id = provider_obj.id

        utility_type = validated_data.get('utility').get('utility_type')
        state = validated_data.get('location').get('state')
        city = validated_data.get('location').get('city')
        utility_obj = Utility.objects.get(utility_type=utility_type)
        print(utility_obj)
        location_obj = Location.objects.get(state=state, city=city)
        unit_measurement = float(validated_data.get('unit_measurement'))
        utility_provider = UtilityProvider(
            utility=utility_obj,
            provider=provider_obj,
            location=location_obj,
            unit_measurement=unit_measurement
        )

        utility_provider.save()
        print(utility_provider.id)
        provider_obj.utility_provider.add(utility_obj)
        #provider_obj.save()
        return provider_obj

    def update(self, instance, validated_data):
        print(instance.utility_provider)
        provider = Provider.objects.get(name=instance.name)
        Provider.objects.filter(id=provider.id).update(name=validated_data.get('name'))

        utility_details = validated_data.pop('utilityprovider_set')[0]
        utility_type = utility_details.get('utility').get('utility_type')
        state = utility_details.get('location').get('state')
        city = utility_details.get('location').get('city')
        utility_obj = Utility.objects.get(utility_type=utility_type)
        location_obj = Location.objects.get(state=state, city=city)
        provider_obj = Provider.objects.get(name=validated_data.get('name'))
        UtilityProvider.objects.filter(provider=provider_obj).update(
            utility=utility_obj,
            provider=provider_obj,
            location=location_obj,
            unit_measurement=float(
                utility_details[
                    'unit_measurement']))
        return provider_obj


class ProviderSerializer(serializers.ModelSerializer):
    # utility_provider = UtilityProviderSerializer(
    #    source="utilityprovider_set", many=True)

    class Meta:
        model = Provider
        fields = ['name']
    #    fields = ['name', 'utility_provider']
    #
    # def to_representation(self, instance):
    #     method = self.context['request'].method
    #     print("in to_representation: ", instance, "--", type(instance), "--", instance.name, "--",
    #           instance.utility_provider)
    #     if method == 'POST' or method == 'PUT':
    #         pass
    #     return serializers.Serializer.to_representation(self, instance)

    # def create(self, validated_data):
    #     utility_provider_data = validated_data.pop('utilityprovider_set')
    #     provider = Provider.objects.create(**validated_data)
    #     for utility in utility_provider_data:
    #         utility_type = utility.get('utility').get('utility_type')
    #         state = utility.get('location').get('state')
    #         city = utility.get('location').get('city')
    #         utility_obj = Utility.objects.get(utility_type=utility_type)
    #         location_obj = Location.objects.get(state=state, city=city)
    #         utility_provider = UtilityProvider(
    #             utility=utility_obj,
    #             provider=provider,
    #             location=location_obj,
    #             unit_measurement=float(
    #                 utility['unit_measurement'])
    #         )
    #         utility_provider.save()
    #         provider.save()
    #         provider.utility_provider.add(utility_provider)
    #     return provider

    # def update(self, instance, validated_data):
    #     print(instance.utility_provider)
    #     provider = Provider.objects.get(name=instance.name)
    #     Provider.objects.filter(id=provider.id).update(name=validated_data.get('name'))
    #
    #     utility_details = validated_data.pop('utilityprovider_set')[0]
    #     utility_type = utility_details.get('utility').get('utility_type')
    #     state = utility_details.get('location').get('state')
    #     city = utility_details.get('location').get('city')
    #     utility_obj = Utility.objects.get(utility_type=utility_type)
    #     location_obj = Location.objects.get(state=state, city=city)
    #     provider_obj = Provider.objects.get(name=validated_data.get('name'))
    #     UtilityProvider.objects.filter(provider=provider_obj).update(
    #                                                         utility=utility_obj,
    #                                                         provider=provider_obj,
    #                                                         location=location_obj,
    #                                                         unit_measurement=float(
    #                                                             utility_details[
    #                                                                 'unit_measurement']))
    #     return provider_obj
    #
    # def delete(self, instance):
    #     UtilityProvider.objects.filter(provider=instance).delete()
    #     instance.save()
    #     return instance
