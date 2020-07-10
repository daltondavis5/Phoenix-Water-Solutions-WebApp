from rest_framework import serializers

from django.db.models import Sum
from core.models.tenant import Tenant, TenantCharge, Payment, \
    PaymentMethod, TenantChargePayment
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

    def calculate_advance_from_payments(self, payment):
        through_table_entries = TenantChargePayment.objects.filter(
            payment=payment)
        print("Through Table entries:", through_table_entries)
        if through_table_entries:
            sum_payment_amount = through_table_entries.aggregate(
                Sum('applied_amount')).get('applied_amount__sum')
            print("Sum payment amount:", sum_payment_amount)
        else:
            sum_payment_amount = 0
        advance_amount = payment.payment_amount - sum_payment_amount

        return advance_amount

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
        initial_amount_temp = initial_amount

        print("Payments Queryset:", payments_queryset)
        for payment in payments_queryset:
            if initial_amount_temp > 0:

                advance_amount = self.calculate_advance_from_payments(payment)

                if 0 < advance_amount <= initial_amount_temp:
                    TenantChargePayment.objects.create(
                        payment=payment,
                        tenant_charge=tenant_charge_obj,
                        applied_amount=advance_amount
                    )
                    initial_amount -= advance_amount

                elif 0 < initial_amount_temp < advance_amount:
                    TenantChargePayment.objects.create(
                        payment=payment,
                        tenant_charge=tenant_charge_obj,
                        applied_amount=advance_amount
                    )
                    advance_amount -= advance_amount  # became 0
            else:
                break

        print("Advance Amount left:", initial_amount_temp)

        return tenant_charge_obj


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = ['charges_applied_to']

    def calculate_remaining_amount_for_charge(self, tenant_charge):
        through_table_entries = TenantChargePayment.objects.filter(
            tenant_charge=tenant_charge)
        print("Through Table entries:", through_table_entries)
        if through_table_entries:
            sum_applied_amount = through_table_entries.aggregate(
                Sum('applied_amount')).get('applied_amount__sum')
            print("Sum applied amount:", sum_applied_amount)
        else:
            sum_applied_amount = 0
        remaining_amount = tenant_charge.initial_amount - sum_applied_amount

        return remaining_amount

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
        charges_queryset = TenantCharge.objects.filter(tenant=tenant_id)
        payment_amount_temp = payment_amount

        print("Charges Queryset:", charges_queryset)
        for charge in charges_queryset:
            if payment_amount_temp > 0:

                remaining_amount = self.calculate_remaining_amount_for_charge(charge)

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

        print("Payment Amount left:", payment_amount_temp)
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
