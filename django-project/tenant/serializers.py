from rest_framework import serializers

from core.models.tenant import Tenant, TenantCharge, Payment, \
    PaymentMethod, TenantChargePayment
import tenant.services as services


class TenantSerializer(serializers.ModelSerializer):
    tenant_usage_info = serializers.SerializerMethodField(
        method_name='get_tenant_usage_info'
    )

    @staticmethod
    def get_tenant_usage_info(obj):
        tenant_id = obj.id
        return services.get_tenant_usage_info(tenant_id)

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

    def create(self, validated_data):
        tenant = validated_data.get('tenant')
        initial_amount = validated_data.get('initial_amount')
        description = validated_data.get('description')
        bill_period_end_date = validated_data.get('bill_period_end_date')
        due_date = validated_data.get('due_date')
        priority = validated_data.get('priority')
        created = validated_data.get('created')
        batch_id = validated_data.get('batch_id')

        tenant_charge_obj = TenantCharge.objects.create(
            tenant=tenant,
            initial_amount=initial_amount,
            description=description,
            bill_period_end_date=bill_period_end_date,
            due_date=due_date,
            priority=priority,
            created=created,
            batch_id=batch_id
        )

        tenant_id = tenant.id
        payments_queryset = Payment.objects.filter(tenant=tenant_id)

        for payment in payments_queryset:
            advance_amount = payment.advance_amount
            if advance_amount > 0:
                if 0 < advance_amount <= initial_amount:
                    TenantChargePayment.objects.create(
                        payment=payment,
                        tenant_charge=tenant_charge_obj,
                        applied_amount=advance_amount
                    )
                    advance_amount -= advance_amount

                elif 0 < initial_amount < advance_amount:
                    TenantChargePayment.objects.create(
                        payment=payment,
                        tenant_charge=tenant_charge_obj,
                        applied_amount=initial_amount
                    )
                    advance_amount -= initial_amount
            else:
                break
        return tenant_charge_obj


class PaymentChargeDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer to display information for the charges_applied_to
    field inside PaymentSerializer
    """
    payment = serializers.CharField(source='payment.payment_amount')
    tenant_charge_amount = serializers.CharField(
        source='tenant_charge.initial_amount')
    payment_date = serializers.DateField(source='payment.payment_date')
    due_date = serializers.DateField(source='tenant_charge.due_date')
    description = serializers.CharField(source='tenant_charge.description')

    class Meta:
        model = TenantChargePayment
        fields = ["tenant_charge_amount", "payment", "applied_amount",
                  "payment_date", "due_date", "description"]


class PaymentSerializer(serializers.ModelSerializer):
    charges_applied_to = PaymentChargeDetailsSerializer(
        source="tenantchargepayment_set", many=True,
        read_only=True)

    class Meta:
        model = Payment
        fields = ["id", "payment_date", "payment_amount",
                  "tenant", "payment_method", "charges_applied_to"]
        read_only_fields = ['charges_applied_to']

    def create(self, validated_data):
        payment_amount = validated_data.get('payment_amount')
        payment_date = validated_data.get('payment_date')
        payment_method = validated_data.get('payment_method')
        tenant = validated_data.get('tenant')
        tenant_id = tenant.id

        payment_obj = Payment.objects.create(
            payment_method=payment_method,
            payment_date=payment_date,
            payment_amount=payment_amount,
            tenant=tenant
        )
        charges_queryset = TenantCharge.objects.filter(
            tenant=tenant_id).order_by('due_date', '-priority')
        payment_amount_temp = payment_amount

        for charge in charges_queryset:
            if payment_amount_temp > 0:

                remaining_amount = charge.remaining_amount

                if 0 < remaining_amount <= payment_amount_temp:
                    TenantChargePayment.objects.create(
                        payment=payment_obj,
                        tenant_charge=charge,
                        applied_amount=remaining_amount
                    )
                    payment_amount_temp -= remaining_amount

                elif 0 < payment_amount_temp < remaining_amount:
                    TenantChargePayment.objects.create(
                        payment=payment_obj,
                        tenant_charge=charge,
                        applied_amount=payment_amount_temp
                    )
                    payment_amount_temp -= payment_amount_temp  # became 0
            else:
                break

        return payment_obj


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
