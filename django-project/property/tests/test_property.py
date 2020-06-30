from datetime import datetime
from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Meter, Property, \
    PropertyCityUtilityInfo, MeterRead
from rest_framework import status
from rest_framework.test import APITestCase


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
    UNIT_LIST_URL = reverse('unit-list')

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

    def test_property_list_for_unit(self):
        """ Test to retrieve all units for a given property """
        Unit.objects.create(name="unit 1", property=self.property)
        Unit.objects.create(name="unit 2", property=self.property)
        Unit.objects.create(name="unit 3", property=self.property)

        response = self.client.get(self.UNIT_LIST_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("unit 1", response.data[0]['name'])
        self.assertEqual("unit 2", response.data[1]['name'])
        self.assertEqual("unit 3", response.data[2]['name'])

    def test_unit_create_is_unique(self):
        """ Test to enforce uniqueness of Name & Property for a Unit """

        Unit.objects.create(name="Test Unit", property=self.property)

        payload = {
            "name": "Test Unit",
            "property": self.property.id
        }
        response = self.client.post(self.UNIT_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class MeterViewSetTestCase(APITestCase):
    METER_LIST_URL = reverse('meter-list')
    # METER_READS_URL = reverse('meter-reads')

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

        self.unit = Unit.objects.create(name="Test Unit",
                                        property=self.property)

        self.meter = Meter.objects.create(
            name="Test Meter",
            installed_date=datetime.now(),
            uninstalled_date=datetime.now(),
            utility=self.utility,
            unit=self.unit
        )

    def test_meterread_list_for_meter(self):
        """ Test to get meter reads for a meter """
        MeterRead.objects.create(meter=self.meter,
                                 read_date=datetime.now(),
                                 amount=99)
        MeterRead.objects.create(meter=self.meter,
                                 read_date=datetime.now(),
                                 amount=199)
        MeterRead.objects.create(meter=self.meter,
                                 read_date=datetime.now(),
                                 amount=299)

        url = detail_url_meterread(self.meter.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(99, response.data[0]['amount'])
        self.assertEqual(199, response.data[1]['amount'])
        self.assertEqual(299, response.data[2]['amount'])
