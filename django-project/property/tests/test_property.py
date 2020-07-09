from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Meter, Property, MeterRead, \
    MeterError
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from property.serializers import MeterSerializer, UnitSerializer, \
    MeterReadSerializer, MeterWithLastReadSerializer, MeterErrorSerializer


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

    def detail_url_unit(self, unit_id):
        return reverse("unit-detail", args=[unit_id])

    def get_reverse_url_property(self, arguments):
        return reverse("property-unit-list", args=arguments)

    def test_property_list_for_unit(self):
        """ Test to retrieve all units for a given property """
        unit1 = Unit.objects.create(name="unit 1", property=self.property1)
        unit2 = Unit.objects.create(name="unit 2", property=self.property1)
        unit3 = Unit.objects.create(name="unit 3", property=self.property2)

        response = self.client.get(self.get_reverse_url_property(
            [self.property1.id]))

        serializer1 = UnitSerializer(unit1)
        serializer2 = UnitSerializer(unit2)
        serializer3 = UnitSerializer(unit3)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer1.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer3.data, response.data)

        # Test to retrieve an empty list if the id is wrong
        response = self.client.get(self.get_reverse_url_property([0]))
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unit_create_is_unique(self):
        """ Test to enforce uniqueness of Name & Property for a Unit """

        Unit.objects.create(name="Test Unit", property=self.property1)

        payload = {
            "name": "Test Unit",
            "property": self.property1.id
        }
        response = self.client.post(self.UNIT_LIST_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unit_update(self):
        """ Test to update a unit """

        unit1 = Unit.objects.create(name="Test Unit", property=self.property1)
        payload = {
            "name": "New Test Unit",
            "property": self.property1.id
        }
        url = self.detail_url_unit(unit1.id)
        response = self.client.put(url, payload)
        unit1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(payload.get('name'), response.data['name'])
        self.assertEqual(payload.get('property'), response.data['property'])

    def test_unit_update_property(self):
        """ Test to fail updating property for a unit """

        unit1 = Unit.objects.create(name="Test Unit", property=self.property1)
        payload = {
            "name": "New Test Unit",
            "property": self.property2.id
        }
        url = self.detail_url_unit(unit1.id)
        response = self.client.put(url, payload)
        unit1.refresh_from_db()
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

        self.meter1 = Meter.objects.create(name="Meter Test 1",
                                           utility=self.utility1,
                                           unit=self.unit1,
                                           installed_date="2020-06-29",
                                           uninstalled_date="2020-06-28")
        self.meter2 = Meter.objects.create(name="Meter Test 2",
                                           utility=self.utility2,
                                           unit=self.unit1,
                                           installed_date="2020-06-29",
                                           uninstalled_date="2020-06-28")

        self.meter_read_1 = MeterRead.objects.create(meter=self.meter1,
                                                     read_date=timezone.now(),
                                                     amount=99.5)
        self.meter_read_2 = MeterRead.objects.create(meter=self.meter2,
                                                     read_date=timezone.now(),
                                                     amount=199.5)

        self.meter_error_1 = MeterError.objects.create(meter=self.meter1,
                                                       error_date="2020-06-28",
                                                       description="Test Desc 1",
                                                       repair_date="2020-06-28")
        self.meter_error_2 = MeterError.objects.create(meter=self.meter2,
                                                       error_date="2020-06-28",
                                                       description="Test Desc 2",
                                                       repair_date="2020-06-28")

    def get_reverse_url_unit_meter_list(self, unit_id):
        return reverse("unit-meter-list", args=unit_id)

    def get_reverse_url_meter_meterread_list(self, meter_id):
        return reverse('meter-meterreads-list', args=meter_id)

    def get_reverse_url_meter_metererror_list(self, meter_id):
        return reverse('meter-metererrors-list', args=meter_id)

    def detail_url_meter(self, meter_id):
        return reverse("meter-detail", args=[meter_id])

    def test_unit_list_meter_with_last_read(self):
        """ Test to retrieve all meters for a given unit"""
        meter3 = Meter.objects.create(name="Meter unit 2 water",
                                      utility=self.utility1,
                                      unit=self.unit2,
                                      installed_date="2020-06-29",
                                      uninstalled_date="2020-06-28")
        response = self.client.get(
            self.get_reverse_url_unit_meter_list([self.unit1.id])
        )
        serializer1 = MeterWithLastReadSerializer(self.meter1)
        serializer2 = MeterWithLastReadSerializer(self.meter2)
        serializer3 = MeterWithLastReadSerializer(meter3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer1.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer3.data, response.data)

    def test_meter_list_meterreads(self):
        """ Test case to retrieve all meter reads for a given meter"""
        meter_read_3 = MeterRead.objects.create(meter=self.meter2,
                                                read_date=timezone.now(),
                                                amount=299.5)
        response = self.client.get(
            self.get_reverse_url_meter_meterread_list([self.meter2.id])
        )
        serializer1 = MeterReadSerializer(self.meter_read_1)
        serializer2 = MeterReadSerializer(self.meter_read_2)
        serializer3 = MeterReadSerializer(meter_read_3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer3.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer1.data, response.data)

        # Test to retrieve an empty list if the id is wrong
        response = self.client.get(
            self.get_reverse_url_meter_meterread_list([0])
        )
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_meter_list_metererrors(self):
        """ Test case to retrieve all meter errors for a given meter"""
        meter_error_3 = MeterError.objects.create(meter=self.meter2,
                                                  error_date="2020-06-28",
                                                  description="Test Desc 3")
        response = self.client.get(
            self.get_reverse_url_meter_metererror_list([self.meter2.id])
        )
        serializer1 = MeterErrorSerializer(self.meter_error_1)
        serializer2 = MeterErrorSerializer(self.meter_error_2)
        serializer3 = MeterErrorSerializer(meter_error_3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer3.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer1.data, response.data)

        # Test to retrieve an empty list if the id is wrong
        response = self.client.get(
            self.get_reverse_url_meter_metererror_list([0])
        )
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_meter_update(self):
        """ Test case to upate a meter """
        meter1 = self.meter1
        payload = {
            "name": "Meter Update",
            "uninstalled_date": "2021-06-29",
            "unit": self.unit1.id,
            "installed_date": "2020-06-29",
            "utility": "Water"
        }
        url = self.detail_url_meter(meter1.id)
        response = self.client.put(url, payload)
        meter1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(payload.get('name'), response.data['name'])
        self.assertEqual(payload.get('uninstalled_date'),
                         response.data['uninstalled_date'])
        self.assertEqual(payload.get('installed_date'),
                        response.data['installed_date'])
        self.assertEqual(payload.get('unit'), response.data['unit'])

    def test_meter_update_installed_date(self):
        """ Test to fail changing of installed date for a meter"""
        meter1 = self.meter1
        payload = {
            "name": "Meter Update",
            "uninstalled_date": "2021-06-29",
            "unit": self.unit1.id,
            "installed_date": "2020-06-30",
            "utility": "Water"
        }
        url = self.detail_url_meter(meter1.id)
        response = self.client.put(url, payload)
        meter1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_meter_update_utility(self):
        """ Test to fail changing of utility for a meter"""
        meter1 = self.meter1
        payload = {
            "name": "Meter Update",
            "uninstalled_date": "2021-06-29",
            "unit": self.unit1.id,
            "installed_date": "2020-06-29",
            "utility": "Gas"
        }
        url = self.detail_url_meter(meter1.id)
        response = self.client.put(url, payload)
        meter1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
