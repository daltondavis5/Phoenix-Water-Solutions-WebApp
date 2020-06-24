from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, UtilityProvider
from rest_framework import status
from rest_framework.test import APITestCase


def detail_url_utility_provider(utility_provider_id):
    return reverse("utilityprovider-detail", args=[utility_provider_id])


def detail_url_provider(provider_id):
    return reverse("provider-detail", args=[provider_id])


class ProviderViewSetTestCase(APITestCase):
    PROVIDER_LIST_URL = reverse("provider-list")
    UTILITY_PROVIDER_LIST_URL = reverse("utilityprovider-list")

    def setUp(self):
        self.utility = Utility.objects.create(type="Water")
        self.location = Location.objects.create(city="Phoenix", state="AZ")
        self.provider = Provider.objects.create(name='Test Provider Services')
        self.utility_provider = UtilityProvider.objects.create(utility=self.utility,
                                                               provider=self.provider,
                                                               location=self.location,
                                                               unit_measurement=1234.50)

    def test_provider_list(self):
        response = self.client.get(self.PROVIDER_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_utility_provider_create(self):
        """ Test create functionality for utility provider through table """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        response = self.client.post(self.UTILITY_PROVIDER_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('provider_name'), payload['provider_name'])
        self.assertEqual(response.data.get('utility_type'), payload['utility_type'])
        self.assertEqual(response.data.get('city'), payload['city'])
        self.assertEqual(response.data.get('state'), payload['state'])
        self.assertEqual(response.data.get('unit_measurement'), payload['unit_measurement'])

    def test_utility_provider_create_utility_error(self):
        """ Test to not allow create if utility already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "AQ92839",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        response = self.client.post(self.UTILITY_PROVIDER_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_create_provider_error(self):
        """  Test to not allow create if provider already present """
        payload = {
            "provider_name": "Not there",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        response = self.client.post(self.UTILITY_PROVIDER_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_create_city_error(self):
        """  Test to not allow create if city already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "not there",
            "unit_measurement": 748.0
        }
        response = self.client.post(self.UTILITY_PROVIDER_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_create_state_error(self):
        """  Test to not allow create if state already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "Not there",
            "unit_measurement": 748.0
        }
        response = self.client.post(self.UTILITY_PROVIDER_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_update(self):
        """ Tests the update functionality for utility provider"""
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        utility_provider = self.utility_provider
        url = detail_url_utility_provider(utility_provider.id)
        response = self.client.put(url, payload)
        utility_provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(payload.get('unit_measurement'),
                         response.data['unit_measurement'])

    def test_utility_provider_update_provider_error(self):
        """  Test to not allow update if provider already present """
        payload = {
            "provider_name": "Provider not there",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        utility_provider = self.utility_provider
        url = detail_url_utility_provider(utility_provider.id)
        response = self.client.put(url, payload)
        utility_provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_update_utility_error(self):
        """  Test to not allow update if utility already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Not there",
            "city": "Phoenix",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        utility_provider = self.utility_provider
        url = detail_url_utility_provider(utility_provider.id)
        response = self.client.put(url, payload)
        utility_provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_update_city_error(self):
        """  Test to not allow update if city already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Not there",
            "state": "AZ",
            "unit_measurement": 748.0
        }
        utility_provider = self.utility_provider
        url = detail_url_utility_provider(utility_provider.id)
        response = self.client.put(url, payload)
        utility_provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_utility_provider_update_state_error(self):
        """  Test to not allow update if state already present """
        payload = {
            "provider_name": "Test Provider Services",
            "utility_type": "Water",
            "city": "Phoenix",
            "state": "Not there",
            "unit_measurement": 748.0
        }
        utility_provider = self.utility_provider
        url = detail_url_utility_provider(utility_provider.id)
        response = self.client.put(url, payload)
        utility_provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_provider_update(self):
        """ Tests the update functionality for provider. Only update Name """
        payload = {
            "name": "Test Provider Services Updated",
        }
        provider = self.provider
        url = detail_url_provider(provider.id)
        response = self.client.put(url, payload)
        provider.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(payload['name'], response.data['name'])


class UtilityViewSetTestCase(APITestCase):
    UTILITY_LIST_URL = reverse('utility-list')

    def test_utility_list(self):
        Utility.objects.create(type="Water")
        Utility.objects.create(type="Electricity")
        response = self.client.get(self.UTILITY_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Water",
                         response.data[0]['type'])
        self.assertEqual("Electricity",
                         response.data[1]['type'])
