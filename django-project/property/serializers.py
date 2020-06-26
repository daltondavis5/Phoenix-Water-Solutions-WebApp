from rest_framework import serializers
from core.models.property import Meter, Property, Unit, \
    PropertyCityUtilityInfo


class MeterSerializer(serializers.ModelSerializer):
    utility_type = serializers.CharField(source='utility.type')
    unit_name = serializers.CharField(source='unit.name')

    class Meta:
        model = Meter
        fields = ['id', 'name', 'installed_date', 'uninstalled_date',
                  'utility_type', 'unit_name']


class PropertyCityUtilityInfoSerializer(serializers.ModelSerializer):
    utility_provider = serializers.CharField(
        source='utility_provider.provider.name')

    class Meta:
        model = PropertyCityUtilityInfo
        fields = ['utility_provider', 'allowance_units', 'bill_period_day',
                  'bill_post_day', 'default_usage']


class PropertySerializer(serializers.ModelSerializer):
    city_utility = PropertyCityUtilityInfoSerializer(
        source='propertycityutilityinfo_set', many=True,
        read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'street_address', 'zip_code',
                  'attribute', 'city_utility']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'zip_code'],
            )
        ]


class UnitSerializer(serializers.ModelSerializer):
    # property_name = serializers.CharField(source='property.name')

    class Meta:
        model = Unit
        fields = ['id', 'name', 'property']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'property'],
            )
        ]
