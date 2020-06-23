from django.test import TestCase

from core.models.utilityprovider import Utility, Provider, UtilityProvider, \
    Location


class ModelCreateTests(TestCase):

    def setUp(self):
        self.utility1 = Utility.objects.create(type='Water')
        self.utility2 = Utility.objects.create(type='Electricity')

        self.location = Location.objects.create(city='Phoenix', state='AZ')

        self.provider = Provider.objects.create(name='Phoenix supplies')

        UtilityProvider.objects.create(
            utility=self.utility1,
            provider=self.provider,
            location=self.location,
            unit_measurement=500)

        UtilityProvider.objects.create(
            utility=self.utility2,
            provider=self.provider,
            location=self.location,
            unit_measurement=50)

    def test_create_utility(self):
        """Test creating utility"""
        utility1 = Utility.objects.get(type='Water')
        utility2 = Utility.objects.get(type='Electricity')
        self.assertEqual(utility1.type, 'Water')
        self.assertEqual(utility2.type, 'Electricity')

    def test_create_location(self):
        """Test creating location"""
        location = Location.objects.get(city='Phoenix', state='AZ')
        self.assertEqual(location.city, 'Phoenix')
        self.assertEqual(location.state, 'AZ')

    def test_create_provider(self):
        """Test creating provider"""
        provider = Provider.objects.get(name='Phoenix supplies')
        self.assertEqual(provider.name, 'Phoenix supplies')

    def test_both_utilities_added(self):
        """Test if multiple utilities are added to provider"""
        utility_attributes1 = {
            'utility': self.utility1,
            'provider': self.provider,
            'location': self.location,
            'unit_measurement': 500
        }

        utility_attributes2 = {
            'utility': self.utility2,
            'provider': self.provider,
            'location': self.location,
            'unit_measurement': 50
        }

        utilityProvider1 = UtilityProvider.objects.get(**utility_attributes1)
        utilityProvider2 = UtilityProvider.objects.get(**utility_attributes2)
        provider = Provider.objects.get(name='Phoenix supplies')
        self.assertIn(utilityProvider1.utility,
                      provider.utilities.all())
        self.assertIn(utilityProvider2.utility,
                      provider.utilities.all())

    def test_no_extra_utility_added(self):
        """Test if utilities are exclusive for different providers"""
        utility_attributes1 = {
            'utility': self.utility1,
            'provider': self.provider,
            'location': self.location,
            'unit_measurement': 500
        }

        utility3 = Utility.objects.create(type='Gas')

        new_provider = Provider.objects.create(name='New provider')

        utility_attributes3 = {
            'utility': utility3,
            'provider': new_provider,
            'location': self.location,
            'unit_measurement': 100
        }

        utilityProvider1 = UtilityProvider.objects.get(**utility_attributes1)
        utilityProvider3 = UtilityProvider.objects.create(
            **utility_attributes3)
        provider = Provider.objects.get(name='Phoenix supplies')
        self.assertIn(utilityProvider1.utility,
                      provider.utilities.all())
        self.assertNotIn(utility3, provider.utilities.all())
        self.assertIn(utility3, new_provider.utilities.all())

    def test_utility_str(self):
        """Check utility string representations"""
        self.assertEqual(str(self.utility1), self.utility1.type)

    def test_location_str(self):
        """Check location string representation"""
        self.assertEqual(str(self.location),
                         self.location.city + ", " + self.location.state)

    def test_provider_str(self):
        """Check provider string representation"""
        self.assertEqual(str(self.provider), self.provider.name)

    def test_utility_provider_str(self):
        """Check utility provider string representation"""
        utility_attributes1 = {
            'utility': self.utility1,
            'provider': self.provider,
            'location': self.location,
            'unit_measurement': 500
        }
        utilityProvider1 = UtilityProvider.objects.get(**utility_attributes1)
        self.assertEqual(str(utilityProvider1), str(utilityProvider1.provider) +
                         " supplies " + str(utilityProvider1.utility) +
                         " in " + str(utilityProvider1.location))
