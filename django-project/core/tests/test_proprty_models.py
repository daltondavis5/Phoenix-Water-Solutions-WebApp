from datetime import datetime
from django.test import TestCase

from core.models.property import Property, PropertyCityUtilityInfo,\
    Unit, Meter
from core.models.utilityprovider import Utility, Location, UtilityProvider,\
    Provider


class ModelCreateTests(TestCase):

    def setUp(self) -> None:
        self.utility = Utility.objects.create(type='Water')
        self.location = Location.objects.create(city='Phoenix', state='AZ')
        self.provider = Provider.objects.create(name='Phoenix supplies')
        self.utility_provider = UtilityProvider.objects.create(
            utility=self.utility,
            provider=self.provider,
            location=self.location,
            unit_measurement=500)

    def test_create_property_and_str(self):
        """ Test to create a new property and str"""
        name = "Property Test"
        street_address = "9999 Test Paradise"
        zip_code = 99999
        attribute = False
        property_ = Property.objects.create(
            name=name,
            street_address=street_address,
            attribute=attribute,
            zip_code=zip_code
        )
        self.assertEqual(property_.name, name)
        self.assertEqual(property_.street_address, street_address)
        self.assertEqual(property_.zip_code, zip_code)
        self.assertEqual(property_.attribute, attribute)
        self.assertEqual(str(property_), name)

    def test_create_unit_and_str(self):
        """ Test to create a new Unit and str"""
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        unit_name = "Unit Test"
        unit = Unit.objects.create(name=unit_name,
                                   property=property_)
        self.assertEqual(unit.property, property_)
        self.assertEqual(unit.name, unit_name)
        self.assertEqual(str(unit), unit_name)

    def test_create_meter_and_str(self):
        """ Test to create meter and str """
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        unit = Unit.objects.create(name="Unit Test",
                                   property=property_)
        meter_name = "Meter Test"
        installed_date = datetime.now()
        uninstalled_date = datetime.now()
        meter = Meter.objects.create(
            name=meter_name,
            utility=self.utility,
            unit=unit,
            installed_date=installed_date,
            uninstalled_date=uninstalled_date
        )
        self.assertEqual(meter.unit, unit)
        self.assertEqual(meter.name, meter_name)
        self.assertEqual(meter.installed_date, installed_date)
        self.assertEqual(meter.uninstalled_date, uninstalled_date)
        self.assertEqual(str(meter), meter_name)

    def test_create_propertcityutilityinfo_create(self):
        """ Test to create PropertyCityUtilityInfo """
        utility_provider = self.utility_provider
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        allowance_units = 4.5
        bill_period_day = 8
        bill_post_day = 8
        default_usage = 10
        property_city_utility_info = PropertyCityUtilityInfo.objects.create(
            utility_provider=utility_provider,
            property=property_,
            allowance_units=allowance_units,
            bill_period_day=bill_period_day,
            bill_post_day=bill_post_day,
            default_usage=default_usage
        )
        self.assertEqual(property_city_utility_info.utility_provider,
                         utility_provider)
        self.assertEqual(property_city_utility_info.property, property_)
        self.assertEqual(property_city_utility_info.allowance_units,
                         allowance_units)
        self.assertEqual(property_city_utility_info.bill_period_day,
                         bill_period_day)
        self.assertEqual(property_city_utility_info.bill_post_day,
                         bill_post_day)
        self.assertEqual(property_city_utility_info.default_usage,
                         default_usage)
