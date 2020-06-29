from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core.models.utilityprovider import UtilityProvider, Utility


class Property(models.Model):
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    attribute = models.BooleanField(default=False)
    city_utility = models.ManyToManyField(UtilityProvider,
                                          through='PropertyCityUtilityInfo')

    def __str__(self):
        return self.name

    class meta:
        unique_together = ('name', 'zip_code')


class PropertyCityUtilityInfo(models.Model):
    utility_provider = models.ForeignKey(UtilityProvider,
                                         on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    allowance_units = models.FloatField()
    bill_period_day = models.PositiveIntegerField(validators=[
        MaxValueValidator(31),
        MinValueValidator(1)
    ])
    bill_post_day = models.PositiveIntegerField(validators=[
        MaxValueValidator(31),
        MinValueValidator(1)
    ])
    default_usage = models.FloatField()


class Unit(models.Model):
    name = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class meta:
        unique_together = ('name', 'property')


class Meter(models.Model):
    name = models.CharField(max_length=50)
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    installed_date = models.DateField()
    uninstalled_date = models.DateField()

    def __str__(self):
        return self.name


class MeterRead(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    read_date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.meter)


class MeterError(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    error_date = models.DateField()
    description = models.CharField(max_length=200)
    repair_date = models.DateField()

    def __str__(self):
        return str(self.meter)


class NewAccountFee(models.Model):
    PRIORITIES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
    )

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITIES)

    def __str__(self):
        return self.name


class LateFee(models.Model):
    PRIORITIES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
    )

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    days_late = models.IntegerField()
    priority = models.IntegerField(choices=PRIORITIES)

    def __str__(self):
        return self.name


class AdminFee(models.Model):
    PRIORITIES = (
        (0, 'Low'),
        (1, 'Normal'),
        (2, 'High'),
    )

    name = models.CharField(max_length=100)
    amount = models.FloatField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITIES)

    def __str__(self):
        return self.name
