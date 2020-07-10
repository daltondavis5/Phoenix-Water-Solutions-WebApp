from rest_framework import serializers

from core.models.tenant import Tenant, TenantCharge, Payment, \
    PaymentMethod
import tenant.services as services


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

    def validate(self, data):
        instance = self.instance
        move_out_date = data.get('move_out_date')
        move_in_date = data.get('move_in_date')

        # if objects exists in db (Update query)
        if instance is not None:
            # check if move out date is greater than move in date
            if move_out_date:
                if move_in_date > move_out_date:
                    raise serializers.ValidationError({
                        'Move out date should be after move ind date.'
                    })

            # do not allow to change move in date
            if instance.move_in_date != move_in_date:
                raise serializers.ValidationError({
                    'Move in date': 'You must not change this field.'
                })

        return data


class TenantChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantCharge
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    payment_method = serializers.CharField(source='payment_method.name')

    class Meta:
        model = Payment
        fields = ['id', 'tenant', 'payment_date', 'payment_amount',
                  'applied_amount', 'payment_method', 'charges_applied_to']


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class TenantUsageSerializer(serializers.ModelSerializer):
    tenant_usage_info = serializers.SerializerMethodField(
        method_name='get_tenant_usage_info'
    )

    class Meta:
        model = Tenant
        fields = ['id', 'first_name', 'last_name', 'primary_email',
                  'secondary_email', 'account_number', 'primary_phone_number',
                  'secondary_phone_number', 'unit', 'move_in_date',
                  'move_out_date', 'credits', 'late_fee_exemption',
                  'tenant_usage_info']

    @staticmethod
    def get_tenant_usage_info(obj):
        tenant_id = obj.id
        return services.get_tenant_usage_info(tenant_id)
