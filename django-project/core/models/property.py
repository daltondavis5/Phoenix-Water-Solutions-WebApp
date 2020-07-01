from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core.models.utilityprovider import UtilityProvider, Utility
from django.utils import timezone


class Property(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    zip_code = models.IntegerField(null=False)
    attribute = models.BooleanField(default=False)
    utility_provider = models.ManyToManyField(UtilityProvider,
                              through='PropertyUtilityProviderInfo')

    def __str__(self):
        return self.name

    class meta:
        unique_together = ('name', 'zip_code')


class PropertyUtilityProviderInfo(models.Model):
    utility_provider = models.ForeignKey(UtilityProvider,
                                         on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    allowance_units = models.FloatField(default=0)
    bill_period_day = models.PositiveIntegerField(validators=[
        MaxValueValidator(31),
        MinValueValidator(1)
    ])
    bill_post_day = models.PositiveIntegerField(validators=[
        MaxValueValidator(31),
        MinValueValidator(1)
    ])
    default_usage = models.FloatField(null=False)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    billing_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class meta:
        unique_together = ('name', 'property')


class Meter(models.Model):
    name = models.CharField(max_length=50)
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    installed_date = models.DateField(default=timezone.now)
    uninstalled_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class MeterRead(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    read_date = models.DateTimeField(null=False)
    amount = models.FloatField(null=False)

    def __str__(self):
        return "Meter: " + str(self.meter) + ", Read Date: " + \
               str(self.read_date) + ", Amount: " + str(self.amount)


class MeterError(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    error_date = models.DateField(null=False)
    description = models.TextField(max_length=200)
    repair_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Meter: " + str(self.meter) + ", Error Date: " + \
               str(self.error_date) + ", Description: " + \
               str(self.description)


class Priority(models.IntegerChoices):
    Low = 0
    Normal = 1
    High = 2


class NewAccountFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=Priority.choices)

    def __str__(self):
        return self.name


class LateFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    days_late = models.IntegerField(null=False)
    priority = models.IntegerField(choices=Priority.choices, null=False)

    def __str__(self):
        return self.name


class AdminFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=Priority.choices)

    def __str__(self):
        return self.name


class RecollectionFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=False)
    usage_based_split = models.BooleanField(default=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=Priority.choices)

    def __str__(self):
        return self.name
