from core.models.tenant import Tenant, TenantCharge, Payment
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


def get_tenants_for_unit(unit_id):
    """
    Method to retrieve all tenants in a unit.
    :param unit_id: unit_id
    :return queryset: all tenants for a unit
    """
    try:
        queryset = Tenant.objects.filter(unit=unit_id)
        return queryset
    except (ObjectDoesNotExist, ValueError):
        return None


def get_current_balance_for_tenant(tenant_id):
    """
    Method to retrieve current balance for a tenant.
    Current balance is the sum of all remaining amount which
    is greater than zero.
    :param tenant_id: tenant id
    :return curr_bal: current balance
    """
    try:
        curr_bal = 0.0
        tenants = TenantCharge.objects.filter(
            tenant=tenant_id, remaining_amount__gt=0). \
            values('remaining_amount')
        if tenants:
            curr_bal = sum([tenants[i].get('remaining_amount')
                            for i in range(len(tenants))])
        return curr_bal
    except (ObjectDoesNotExist, ValueError):
        return 0.0


def get_overdue_balance_for_tenant(tenant_id):
    """
    Method to retrieve overdue balance for a tenant.
    Current balance is the sum of all remaining amount which
    is greater than zero and has passed the due date.
    :param tenant_id: tenant id
    :return overdue_bal: overdue balance
    """
    try:
        overdue_bal = 0.0
        today = timezone.now().date()
        tenants = TenantCharge.objects.filter(
            tenant=tenant_id, remaining_amount__gt=0, due_date__lt=today). \
            values('remaining_amount')
        if tenants:
            overdue_bal = sum([tenants[i].get('remaining_amount')
                               for i in range(len(tenants))])
        return overdue_bal
    except (ObjectDoesNotExist, ValueError):
        return 0.0


def get_tenant_usage_info(tenant_id):
    """
    Method to retrieve tenant usage info which includes
    current balance and overdue balance.
    :param tenant_id: tenant id
    :return tenant_usage_info: tenant usage info
    """
    curr_balance = get_current_balance_for_tenant(tenant_id)
    overdue_balance = get_overdue_balance_for_tenant(tenant_id)
    tenant_usage_info = ["current_balance:" + str(curr_balance),
                         "overdue_balance:" + str(overdue_balance)]
    return tenant_usage_info


def get_charges_for_tenant(tenant_id):
    try:
        queryset = TenantCharge.objects.filter(tenant=tenant_id)
        return queryset
    except (ObjectDoesNotExist, ValueError):
        return None


def get_payments_for_tenant(tenant_id):
    try:
        queryset = Payment.objects.filter(
            tenant=tenant_id).order_by('-payment_date')
        return queryset
    except (ObjectDoesNotExist, ValueError):
        return None
