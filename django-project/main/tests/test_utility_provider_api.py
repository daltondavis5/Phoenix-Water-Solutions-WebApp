import json

from django.urls import reverse

from core.models.utilityprovider import *
from main.serializers.utilityprovider import ProviderSerializer
from rest_framework import status
from rest_framework.test import APITestCase


class ProviderViewSetTestCase(APITestCase):
    list_url = reverse("provider-list")

    def setUp(self):
        Utility.objects.create(utility_type="Water")
        Location.objects.create(city="Phoenix", state="AZ")

    def test_provider_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_create(self):
        data = {
            "name": "Test Provider",
            "utility_provider": [
                {
                    "utility": {
                        "utility_type": "Water"
                    },
                    "location": {
                        "city": "Phoenix",
                        "state": "AZ"
                    },
                    "unit_measurement": 900.0
                }
            ]
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['provider'].get('name'), data['name'])
