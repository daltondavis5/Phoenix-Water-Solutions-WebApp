from django.db import models

from core.models.property import Unit, Priority


class Tenant(models.Model):
    account_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    primary_phone_number = models.CharField(max_length=15)
    secondary_phone_number = models.CharField(max_length=15)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)
    credits = models.FloatField()
    late_fee_exemption = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Tenant Name:" + str(self.first_name) + " Primary Phone:" + \
            str(self.primary_phone_number)


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
    created = models.DateTimeField()
    batch_id = models.PositiveIntegerField()

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + ", Phone: " + \
                str(self.tenant.primary_phone_number) + ", " \
                "Due Date: " + str(self.due_date)


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    applied_amount = models.FloatField()
    payment_method = models.ForeignKey(PaymentMethod,
                                       on_delete=models.CASCADE)
    charges_applied_to = models.ManyToManyField(TenantCharge,
                                                through='TenantChargePayment')

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + \
               ", Payment Amount: " + str(self.payment_amount)


class TenantChargePayment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    tenant_charge = models.ForeignKey(TenantCharge, on_delete=models.CASCADE)


class TenantNotes(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    date_logged = models.DateField()
    note = models.TextField(max_length=200)

    def __str__(self):
        return "Tenant: " + str(self.tenant.first_name) + \
               " ,Date Logged:" + str(self.date_logged)
