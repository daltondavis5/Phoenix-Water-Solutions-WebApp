from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Meter, Property, Unit, \
    MeterRead, MeterError
from django.utils import timezone
import property.services as services
from rest_framework.test import APITestCase
from core.exceptions.exceptions import NonNumericalValueException, \
    InvalidIDException


class PropertyServicesTestCase(APITestCase):

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
        self.unit1 = Unit.objects.create(
            name="Unit 1", property=self.property)
        self.unit2 = Unit.objects.create(
            name="Unit 2", property=self.property)
        self.meter1 = \
            Meter.objects.create(name="Meter Test 1",
                                 utility=self.utility,
                                 unit=self.unit1,
                                 installed_date=timezone.now().date(),
                                 uninstalled_date=timezone.now().date() +
                                 timezone.timedelta(days=10))
        self.meter2 = \
            Meter.objects.create(name="Meter Test 2",
                                 utility=self.utility,
                                 unit=self.unit1,
                                 installed_date=timezone.now().date() +
                                 timezone.timedelta(days=1),
                                 uninstalled_date=timezone.now().date() +
                                 timezone.timedelta(days=10))

        self.meter_read_1 = MeterRead.objects.create(meter=self.meter1,
                                                     read_date=timezone.now(),
                                                     amount=99.5)
        self.meter_read_2 = MeterRead.objects.create(meter=self.meter1,
                                                     read_date=timezone.now(),
                                                     amount=199.5)

        self.meter_error_1 = \
            MeterError.objects.create(meter=self.meter2,
                                      error_date=timezone.now().date(),
                                      description="Test Desc 1",
                                      repair_date=timezone.now().date() +
                                      timezone.timedelta(days=10))
        self.meter_error_2 = \
            MeterError.objects.create(meter=self.meter2,
                                      error_date=timezone.now().date() +
                                      timezone.timedelta(
                                          days=1),
                                      description="Test Desc 10",
                                      repair_date=timezone.now().date() +
                                      timezone.timedelta(days=10))

    def test_get_meters_for_unit(self):
        """ Test to get all meters for a unit """
        unit_id = self.unit1.id
        actual = services.get_meters_for_unit(unit_id)
        self.assertIn(self.meter1, actual)
        self.assertIn(self.meter2, actual)

    def test_fail_get_meters_for_unit_id(self):
        """ Test to fail get all meters for a unit with an
        id for which the object does not exist """
        unit_id = 0
        self.assertRaises(
            InvalidIDException, services.get_meters_for_unit, unit_id)

    def test_fail_get_meters_for_unit_id_type(self):
        """ Test case to fail get all tenants for a unit with
            and invalid id type """
        unit_id = "s"
        self.assertRaises(
            NonNumericalValueException, services.get_meters_for_unit, unit_id)

    def test_get_meter_reads_for_meter(self):
        """ Test to get all meter reads for a meter """
        meter_id = self.meter1.id
        actual = services.get_meter_reads_for_meter(meter_id)
        self.assertIn(self.meter_read_1, actual)
        self.assertIn(self.meter_read_2, actual)

    def test_fail_get_meter_reads_for_meter_id(self):
        """ Test to fail get all meter reads for a meter with an
        id for which the object does not exist """
        meter_id = 0
        self.assertRaises(InvalidIDException,
                          services.get_meter_reads_for_meter, meter_id)

    def test_fail_get_meter_reads_for_meter_id_type(self):
        """ Test case to fail get all meter reads for a meter with
            and invalid id type """
        meter_id = "s"
        self.assertRaises(NonNumericalValueException,
                          services.get_meter_reads_for_meter, meter_id)

    def test_get_meter_errors_for_meter(self):
        """ Test to get all meter errors for a meter """
        meter_id = self.meter2.id
        actual = services.get_meter_errors_for_meter(meter_id)
        self.assertIn(self.meter_error_1, actual)
        self.assertIn(self.meter_error_2, actual)

    def test_fail_get_meter_errors_for_meter_id(self):
        """ Test to fail get all meter errors for a meter with an
        id for which the object does not exist """
        meter_id = 0
        self.assertRaises(InvalidIDException,
                          services.get_meter_errors_for_meter, meter_id)

    def test_fail_get_meter_errors_for_meter_id_type(self):
        """ Test case to fail get all meter errors for a meter with
            and invalid id type """
        meter_id = "s"
        self.assertRaises(NonNumericalValueException,
                          services.get_meter_errors_for_meter, meter_id)

    def test_get_units_for_property(self):
        """ Test to get all units for a property """
        property_id = self.property.id
        actual = services.get_units_for_property(property_id)
        self.assertIn(self.unit1, actual)
        self.assertIn(self.unit2, actual)

    def test_fail_get_units_for_property_id(self):
        """ Test to fail get all units for a property with an
        id for which the object does not exist """
        property_id = 0
        self.assertRaises(InvalidIDException,
                          services.get_units_for_property, property_id)

    def test_fail_get_units_for_property_id_type(self):
        """ Test case to fail get all units for a property with
            and invalid id type """
        property_id = "s"
        self.assertRaises(NonNumericalValueException,
                          services.get_units_for_property, property_id)
