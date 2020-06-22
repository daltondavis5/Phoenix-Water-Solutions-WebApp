from django.urls import reverse

from core.models.utilityprovider import Utility, Location
from rest_framework import status
from rest_framework.test import APITestCase


class ProviderViewSetTestCase(APITestCase):
    PROVIDER_LIST_URL = reverse("provider-list")

    def setUp(self):
        Utility.objects.create(utility_type="Water")
        Location.objects.create(city="Phoenix", state="AZ")

    def test_provider_list(self):
        response = self.client.get(self.PROVIDER_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_create(self):
        data = {
            "name": "Test Provider",
            "utility_provider": [
                {
                    "utility_type": "Water",
                    "city": "Phoenix",
                    "state": "AZ",
                    "unit_measurement": 748.0
                }
            ]
        }
        response = self.client.post(self.PROVIDER_LIST_URL, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['provider'].get('name'), data['name'])

    def test_provider_update(self):
        """ Tests the update functionality for provider """
        data = {
            "name": "Test Provider",
            "utility_provider": [
                {
                    "utility_type": "Water",
                    "city": "Phoenix",
                    "state": "AZ",
                    "unit_measurement": 748.0
                }
            ]
        }


class UtilityViewSetTestCase(APITestCase):
    UTILITY_LIST_URL = reverse('utility-list')

    def test_utility_list(self):
        Utility.objects.create(utility_type="Water")
        Utility.objects.create(utility_type="Electricity")
        response = self.client.get(self.UTILITY_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("Water",
                         response.data['utilities'][0]['utility_type'])
        self.assertEqual("Electricity",
                         response.data['utilities'][1]['utility_type'])
