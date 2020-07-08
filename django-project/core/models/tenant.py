from django.db import models

from core.models.property import Unit, Priority
from django.utils import timezone


class Tenant(models.Model):
    account_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    primary_email = models.EmailField()
    secondary_email = models.EmailField(null=True, blank=True)
    primary_phone_number = models.CharField(max_length=15)
    secondary_phone_number = models.CharField(max_length=15,
                                              null=True, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)
    credits = models.FloatField(null=True, blank=True)
    late_fee_exemption = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Tenant Name:" + str(self.first_name) + ", Primary Email:" + \
               str(self.primary_email) + ", Unit:" + str(self.unit.name)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return "Payment Method: " + str(self.name)


class TenantCharge(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    initial_amount = models.FloatField()
    remaining_amount = models.FloatField()
    description = models.CharField(max_length=100)
    bill_period_end_date = models.DateField()
    due_date = models.DateField()
    priority = models.IntegerField(choices=Priority.choices)
    created = models.DateTimeField(default=timezone.now)
    batch_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + \
               ", Due Date: " + str(self.due_date) + ", Initial Amount: " \
               + str(self.initial_amount) + ", Remaining Amount: " + \
               str(self.remaining_amount)


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_date = models.DateField(default=timezone.now)
    payment_amount = models.FloatField()
    applied_amount = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod,
                                       on_delete=models.CASCADE)
    charges_applied_to = models.ManyToManyField(TenantCharge,
                                                through='TenantChargePayment')

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + \
               ", Payment Amount: " + str(self.payment_amount) + \
               ", Payment Date:  " + str(self.payment_date)


class TenantChargePayment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    tenant_charge = models.ForeignKey(TenantCharge, on_delete=models.CASCADE)


class TenantNotes(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    date_logged = models.DateField(default=timezone.now)
    note = models.TextField(max_length=200)

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + \
               " ,Date Logged:" + str(self.date_logged)
