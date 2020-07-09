from core.models.property import Unit
from core.models.tenant import Tenant, TenantCharge, Payment
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from core.exceptions.exceptions import NonNumericalException, NonValidID


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
    except (ObjectDoesNotExist):
        raise NonValidID
    except(ValueError):
        raise NonNumericalException


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
        curr_bal = 0.0
        charges = TenantCharge.objects.filter(
            tenant=tenant.id, remaining_amount__gt=0). \
            values('remaining_amount')
        if charges:
            curr_bal = sum([charges[i].get('remaining_amount')
                            for i in range(len(charges))])
        return curr_bal
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


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
        overdue_bal = 0.0
        today = timezone.now().date()
        charges = TenantCharge.objects.filter(
            tenant=tenant.id, remaining_amount__gt=0, due_date__lt=today). \
            values('remaining_amount')
        if charges:
            overdue_bal = sum([charges[i].get('remaining_amount')
                               for i in range(len(charges))])
        return overdue_bal
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_tenant_usage_info(tenant_id):
    """
    Method to retrieve tenant usage info which includes
    current balance and overdue balance.
    :param tenant_id: tenant id
    :return tenant_usage_info: tenant usage info
    """
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        curr_balance = get_current_balance_for_tenant(tenant.id)
        overdue_balance = get_overdue_balance_for_tenant(tenant.id)
        tenant_usage_info = [{"current_balance": curr_balance,
                              "overdue_balance": overdue_balance}]
        return tenant_usage_info
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_charges_for_tenant(tenant_id):
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        queryset = TenantCharge.objects.filter(tenant=tenant)
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_payments_for_tenant(tenant_id):
    try:
        tenant = Tenant.objects.get(pk=tenant_id)
        queryset = Payment.objects.filter(
            tenant=tenant).order_by('-payment_date')
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")
