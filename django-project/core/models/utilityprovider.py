from django.db import models


class Utility(models.Model):
    utility_type = models.CharField(max_length=50)

    def __str__(self):
        return self.utility_type


class Provider(models.Model):
    name = models.CharField(max_length=50)
    utility_provider = models.ManyToManyField(
        Utility,
        through='UtilityProvider')

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.city + ", " + self.state


class UtilityProvider(models.Model):
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    unit_measurement = models.FloatField()

    def __str__(self):
        return str(self.provider) + " supplies " + str(self.utility) + \
            " in " + str(self.location)