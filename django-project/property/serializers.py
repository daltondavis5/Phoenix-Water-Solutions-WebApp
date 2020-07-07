from rest_framework import serializers
from core.models.property import Meter, Property, Unit, \
    PropertyUtilityProviderInfo, MeterRead, MeterError

import property.services as services


class MeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'unit'],
            )
        ]

    def validate(self, data):
        instance = self.instance
        utility = data.get('utility')
        installed_date = data.get('installed_date')

        # if objects exists in db (Update)
        if instance is not None:
            if installed_date != instance.installed_date \
                    or utility != instance.utility:
                raise serializers.ValidationError({
                    'Utility & Installed Date':
                        'You must not change these fields.'
                })

        return data


class PropertyUtilityProviderInfoSerializer(serializers.ModelSerializer):
    utility_provider = serializers.CharField(
        source='utility_provider.provider.name')

    class Meta:
        model = PropertyUtilityProviderInfo
        fields = ['utility_provider', 'allowance_units', 'bill_period_day',
                  'bill_post_day', 'default_usage']


class PropertySerializer(serializers.ModelSerializer):
    utility_provider = PropertyUtilityProviderInfoSerializer(
        source='propertyutilityproviderinfo_set', many=True,
        read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'street_address', 'zip_code',
                  'attribute', 'utility_provider']
        read_only_fields = ['attribute', 'utility_provider']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'zip_code'],
            )
        ]


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ['id', 'name', 'property']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'property'],
            )
        ]

    def validate(self, data):
        instance = self.instance
        property = data.get('property')

        # if objects exists in db (Update)
        if instance is not None:
            if property != instance.property:
                raise serializers.ValidationError({
                    'property': 'You must not change this field.'
                })

        return data


class MeterReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeterRead
        fields = "__all__"


class MeterErrorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeterError
        fields = "__all__"


class MeterWithLastReadSerializer(serializers.ModelSerializer):
    last_read_info = serializers.SerializerMethodField(
        method_name='get_last_read_info'
    )

    class Meta:
        model = Meter
        fields = ['id', 'name', 'utility', 'unit', 'last_read_info']

    @staticmethod
    def get_last_read_info(obj):
        return services.get_last_read_info_for_meter(obj)
