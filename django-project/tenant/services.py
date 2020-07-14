from core.models.property import Unit
from core.models.tenant import Tenant, TenantCharge, Payment, \
    TenantChargePayment
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.utils import timezone
from core.exceptions.exceptions import NonNumericalValueException, \
    InvalidIDException


def get_tenants_for_unit(unit_id):
    """
    Method to retrieve all tenants in a unit.
    :param unit_id: unit_id
    :return queryset: all tenants for a unit
    """
    try:
        unit = Unit.objects.get(pk=unit_id)
        queryset = Tenant.objects.filter(unit=unit)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_current_balance_for_tenant(tenant_id):
    """
    Method to retrieve current balance for a tenant.
    Current balance is the sum of all remaining amount which
    is greater than zero.
    :param tenant_id: tenant id
    :return curr_bal: current balance
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        charge_queryset = TenantCharge.objects.filter(tenant=tenant)
        payment_queryset = Payment.objects.filter(tenant=tenant)

        """ We calculate the 'remaining balance from all charges (if any)'
        and 'advance payment balance from all payments (if any)' and take
        the difference as current outstanding balance."""
        remaining_amount = 0.0
        for charge in charge_queryset:
            remaining_amount += charge.remaining_amount

        advance_amount = 0.0
        for payment in payment_queryset:
            advance_amount += payment.advance_amount

        curr_bal = remaining_amount - advance_amount

        return curr_bal
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_overdue_balance_for_tenant(tenant_id):
    """
    Method to retrieve overdue balance for a tenant.
    Current balance is the sum of all remaining amount which
    is greater than zero and has passed the due date.
    :param tenant_id: tenant id
    :return overdue_bal: overdue balance
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        today = timezone.now().date()
        charge_queryset = TenantCharge.objects.filter(
            tenant=tenant, due_date__lt=today)
        payment_queryset = Payment.objects.filter(tenant=tenant)

        """ We calculate the 'remaining balance from all charges (if any)'
        and 'advance payment balance from all payments (if any)' and take
        the difference as overdue balance. Charges which are past due date
        are only considered. """
        remaining_amount = 0.0
        for charge in charge_queryset:
            remaining_amount += charge.remaining_amount

        advance_amount = 0.0
        for payment in payment_queryset:
            advance_amount += payment.advance_amount

        overdue_bal = remaining_amount - advance_amount

        return overdue_bal
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_tenant_charge_info(tenant_id):
    """
    Method to retrieve tenant usage info which includes
    current balance and overdue balance.
    :param tenant_id: tenant id
    :return tenant_charge_info: tenant usage info
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        curr_balance = get_current_balance_for_tenant(tenant.id)
        overdue_balance = get_overdue_balance_for_tenant(tenant.id)
        tenant_charge_info = {"current_balance": curr_balance,
                             "overdue_balance": overdue_balance}
        return tenant_charge_info
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_charges_for_tenant(tenant_id):
    """
    Method to retrieve tenant charges info which
    includes all the charges of the tenant.
    :param tenant_id: tenant id
    :return charges: tenant charge info
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        queryset = TenantCharge.objects.filter(tenant=tenant)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_payments_for_tenant(tenant_id):
    """
    Method to retrieve tenant payment info which
    includes all the payments of the tenant.
    :param tenant_id: tenant id
    :return payments: tenant payment info
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        queryset = Payment.objects.filter(
            tenant=tenant).order_by('-payment_date')
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def create_tenant_charge_payment_for_payment(charges_queryset,
                                             payment_object):
    """ This method create row(s) in TenantChargePayment table
        for the given payment, and all those charges for which
        the remaining amount > 0.
    :param charges_queryset: queryset with all the charges
                            for a tenant
    :param payment_object: payment object for which the charges
                        needs to be applied.
    :return: None.
    """
    if not charges_queryset or not payment_object:
        return

    payment_amount = payment_object.payment_amount
    for charge in charges_queryset:
        if payment_amount > 0:

            remaining_amount = charge.remaining_amount

            if 0 < remaining_amount <= payment_amount:
                TenantChargePayment.objects.create(
                    payment=payment_object,
                    tenant_charge=charge,
                    applied_amount=remaining_amount
                )
                payment_amount -= remaining_amount

            elif 0 < payment_amount < remaining_amount:
                TenantChargePayment.objects.create(
                    payment=payment_object,
                    tenant_charge=charge,
                    applied_amount=payment_amount
                )
                payment_amount -= payment_amount  # became 0
        else:
            break


def create_tenant_charge_payment_for_charge(payments_queryset,
                                        tenant_charge_object):
    """ This method create row(s) in TenantChargePayment table
        for the given tenant charge, and all those payments for
        which the advance amount > 0.
    :param payments_queryset: queryset with all the charges
                            for a tenant
    :param tenant_charge_object: payment object for which the charges
                        needs to be applied.
    :return: None.
    """
    if not payments_queryset or not tenant_charge_object:
        return
    initial_amount = tenant_charge_object.initial_amount
    for payment in payments_queryset:
        advance_amount = payment.advance_amount
        if advance_amount > 0:
            if 0 < advance_amount <= initial_amount:
                TenantChargePayment.objects.create(
                    payment=payment,
                    tenant_charge=tenant_charge_object,
                    applied_amount=advance_amount
                )
                advance_amount -= advance_amount

            elif 0 < initial_amount < advance_amount:
                TenantChargePayment.objects.create(
                    payment=payment,
                    tenant_charge=tenant_charge_object,
                    applied_amount=initial_amount
                )
                advance_amount -= initial_amount
