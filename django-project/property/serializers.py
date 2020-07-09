from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from core.models.property import Meter, Property, Unit, \
    PropertyUtilityProviderInfo, MeterRead, MeterError


class MeterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meter
        fields = "__all__"


class PropertyUtilityProviderInfoSerializer(serializers.ModelSerializer):
    utility_provider = serializers.CharField(
        source='utility_provider.provider.name')

    class Meta:
        model = PropertyUtilityProviderInfo
        fields = ['utility_provider', 'allowance_units', 'bill_period_day',
                  'bill_post_day', 'default_usage']


class PropertySerializer(serializers.ModelSerializer):
    city_utility = PropertyUtilityProviderInfoSerializer(
        source='propertyutilityproviderinfo_set', many=True,
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

    class Meta:
        model = Unit
        fields = ['id', 'name', 'property']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['name', 'property'],
            )
        ]


class MeterReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeterRead
        fields = ['id', 'read_date', 'amount']


class MeterErrorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeterError
        fields = "__all__"


class MeterWithLastReadSerializer(serializers.ModelSerializer):
    last_read_info = serializers.SerializerMethodField(
        method_name='get_last_read_info_for_meter'
    )

    class Meta:
        model = Meter
        fields = ['id', 'name', 'utility', 'unit', 'last_read_info']

    def get_last_read_info_for_meter(self, obj):
        try:
            last_read_obj = obj.meterread_set.latest('read_date')
            last_read_info = [last_read_obj.amount, last_read_obj.read_date]
            return last_read_info
        except ObjectDoesNotExist:
            return None


class PropertyMeterReadSerializer(serializers.Serializer):
    property_id = serializers.IntegerField()
    to_date = serializers.DateField()
    from_date = serializers.DateField()
    utility_type = serializers.CharField()

    def validate(self, data):
        if data['from_date'] > data['to_date']:
            raise serializers.ValidationError("from_date can not be "
                                              "greater than to_date.")
        return data
