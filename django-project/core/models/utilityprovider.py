from django.db import models


class Utility(models.Model):
    type = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.type


class Provider(models.Model):
    name = models.CharField(max_length=50, unique=True)
    utilities = models.ManyToManyField(
        Utility,
        through='UtilityProvider')

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.city + ", " + self.state

    class meta:
        unique_together = ('city', 'state')


class UtilityProvider(models.Model):
    utility = models.ForeignKey(Utility, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    unit_measurement = models.FloatField()

    def __str__(self):
        return "Provider: " + str(self.provider) + ", Utility: " + \
               str(self.utility) + ", Location: " + str(self.location)

    class meta:
        unique_together = ('utility', 'provider', 'location')
