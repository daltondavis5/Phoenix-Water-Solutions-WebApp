from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Meter, Property, MeterRead, \
    MeterError
from property import services
from django.utils import timezone
import datetime
from django.conf import settings
from django.db import connection
from rest_framework.test import APITestCase


class PropertyServicesTestCase(APITestCase):

    def setUp(self):
        self.property1 = Property.objects.create(
            name="Property Test 1",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        self.unit1 = Unit.objects.create(name="unit 1", property=self.property1)
        self.unit2 = Unit.objects.create(name="unit 2", property=self.property1)
        self.utility1 = Utility.objects.create(type="Water")
        self.meter1 = Meter.objects.create(name="Meter 1 Unit 1",
                                           utility=self.utility1,
                                           unit=self.unit1,
                                           installed_date="2020-06-29",
                                           uninstalled_date="2020-06-28")
        self.meter2 = Meter.objects.create(name="Meter 1 Unit 2",
                                           utility=self.utility1,
                                           unit=self.unit2,
                                           installed_date="2020-06-29",
                                           uninstalled_date="2020-06-28")
        self.meter3 = Meter.objects.create(name="Meter 2 Unit 2",
                                           utility=self.utility1,
                                           unit=self.unit2,
                                           installed_date="2020-06-29",
                                           uninstalled_date="2020-06-28")
        self.new_read_date = timezone.now()
        self.old_read_date = timezone.now() - \
                             datetime.timedelta(days=2)
        self.old_read_date2 = timezone.now() - \
                              datetime.timedelta(days=1, hours=2)

        self.meter1_read_old = MeterRead.objects.create(
            meter=self.meter1, read_date=self.old_read_date, amount=100)
        self.meter1_read_new = MeterRead.objects.create(
            meter=self.meter1, read_date=self.new_read_date, amount=150)
        self.meter2_read_old = MeterRead.objects.create(
            meter=self.meter2, read_date=self.old_read_date, amount=200)
        self.meter3_read_new = MeterRead.objects.create(
            meter=self.meter3, read_date=self.new_read_date, amount=300)
        self.meter3_read1_old = MeterRead.objects.create(
            meter=self.meter3, read_date=self.old_read_date, amount=100)
        self.meter3_read2_old = MeterRead.objects.create(
            meter=self.meter3, read_date=self.old_read_date2, amount=200)

    def test_get_utility_usage_amount_for_property_pass(self):
        """
        Test to check usage amount with multiple
        meter reads and missing meter reads
        """
        new_date = timezone.now().date()
        old_date = timezone.now().date() - datetime.timedelta(days=2)
        utility_type = "Water"
        # settings.DEBUG = True
        resp = services.get_utility_usage_amount_for_property(
            self.property1, old_date, new_date, utility_type)
        # print("DB connection.queries", len(connection.queries))
        self.assertEqual(resp["to_date_error"][0], self.meter2.name)
        self.assertEqual(resp['amount'], 250)

    def test_get_utility_usage_amount_for_property_fail_no_meters(self):
        """
        Test to check usage amount by passing property
        id that does not return any meters
        """
        to_date = timezone.now().date()
        from_date = timezone.now().date() - datetime.timedelta(days=2)
        utility_type = "Water"
        resp = services.get_utility_usage_amount_for_property(
            22, from_date, to_date, utility_type)
        self.assertEqual(resp['amount'], 0)

    def test_get_utility_usage_amount_for_property_fail_no_meter_reads(self):
        """
        Test to check usage amount by passing dates
        that have no meter reads
        """
        to_date = timezone.now().date() - datetime.timedelta(days=10)
        from_date = timezone.now().date() - datetime.timedelta(days=11)
        utility_type = "Water"
        resp = services.get_utility_usage_amount_for_property(
            self.property1, from_date, to_date, utility_type)
        self.assertEqual(resp['amount'], 0)
