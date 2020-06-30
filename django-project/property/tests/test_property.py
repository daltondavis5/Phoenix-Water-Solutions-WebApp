from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Meter, Property
from rest_framework import status
from rest_framework.test import APITestCase
from property.serializers import MeterSerializer, UnitSerializer


def detail_url_property(property_id):
    return reverse("property-detail", args=[property_id])


def detail_url_unit(unit_id):
    return reverse("unit-detail", args=[unit_id])


def detail_url_meterread(meter_id):
    return reverse("meter-list", args=[meter_id])


class PropertyViewSetTestCase(APITestCase):
    PROPERTY_LIST_URL = reverse("property-list")

    def setUp(self) -> None:
        self.utility = Utility.objects.create(type='Water')
        self.location = Location.objects.create(city='Phoenix', state='AZ')
        self.provider = Provider.objects.create(name='Phoenix supplies')
        self.utility_provider = UtilityProvider.objects.create(
            utility=self.utility,
            provider=self.provider,
            location=self.location,
            unit_measurement=500)

        self.property = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )

    def test_property_create_is_unique(self):
        """ Test to enforce uniqueness of Name & Zip Code for a property """
        payload = {
            "name": "Property Test",
            "street_address": "Paradise Street",
            "zip_code": 99999,
            "attribute": False,
        }
        response = self.client.post(self.PROPERTY_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UnitViewSetTestCase(APITestCase):
    UNIT_LIST_URL = reverse("unit-list")

    def setUp(self) -> None:
        self.utility = Utility.objects.create(type='Water')
        self.location = Location.objects.create(city='Phoenix', state='AZ')
        self.provider = Provider.objects.create(name='Phoenix supplies')
        self.utility_provider = UtilityProvider.objects.create(
            utility=self.utility,
            provider=self.provider,
            location=self.location,
            unit_measurement=500)

        self.property1 = Property.objects.create(
            name="Property Test 1",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )

        self.property2 = Property.objects.create(
            name="Property Test 2",
            street_address="1565 W Drive",
            attribute=False,
            zip_code=86595
        )

    def getReverseURL(self, arguments):
        return reverse("property-unit-list", args=arguments)

    def test_property_list_for_unit(self):
        """ Test to retrieve all units for a given property """
        unit1 = Unit.objects.create(name="unit 1", property=self.property1)
        unit2 = Unit.objects.create(name="unit 2", property=self.property1)
        unit3 = Unit.objects.create(name="unit 3", property=self.property2)

        response = self.client.get(self.getReverseURL([self.property1.id]))

        serializer1 = UnitSerializer(unit1)
        serializer2 = UnitSerializer(unit2)
        serializer3 = UnitSerializer(unit3)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer1.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer3.data, response.data)

    def test_unit_create_is_unique(self):
        """ Test to enforce uniqueness of Name & Property for a Unit """

        Unit.objects.create(name="Test Unit", property=self.property1)

        payload = {
            "name": "Test Unit",
            "property": self.property1.id
        }
        response = self.client.post(self.UNIT_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MeterViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.utility1 = Utility.objects.create(type='Water')
        self.utility2 = Utility.objects.create(type='Gas')
        self.location = Location.objects.create(city='Phoenix', state='AZ')
        self.provider = Provider.objects.create(name='Phoenix supplies')
        self.utility_provider = UtilityProvider.objects.create(
            utility=self.utility1,
            provider=self.provider,
            location=self.location,
            unit_measurement=500)

        self.property = Property.objects.create(
            name="Property Test 1",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )

        self.unit1 = Unit.objects.create(
            name="Unit 1", property=self.property)
        self.unit2 = Unit.objects.create(
            name="Unit 2", property=self.property)

    def getReverseURL(self, arguments):
        return reverse("unit-meter-list", args=arguments)

    def test_meter_list_unit(self):
        """ Test to retrieve all meters for a given unit"""
        meter1 = Meter.objects.create(name="Meter unit 1 water",
                                      utility=self.utility1,
                                      unit=self.unit1,
                                      installed_date="2020-06-29",
                                      uninstalled_date="2020-06-28")
        meter2 = Meter.objects.create(name="Meter unit 1 gas",
                                      utility=self.utility2,
                                      unit=self.unit1,
                                      installed_date="2020-06-29",
                                      uninstalled_date="2020-06-28")
        meter3 = Meter.objects.create(name="Meter unit 2 water",
                                      utility=self.utility1,
                                      unit=self.unit2,
                                      installed_date="2020-06-29",
                                      uninstalled_date="2020-06-28")
        response = self.client.get(self.getReverseURL([self.unit1.id]))
        serializer1 = MeterSerializer(meter1)
        serializer2 = MeterSerializer(meter2)
        serializer3 = MeterSerializer(meter3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer1.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer3.data, response.data)
