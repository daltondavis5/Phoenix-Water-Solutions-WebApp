from django.utils import timezone
from django.test import TestCase

from core.models.property import Property, PropertyUtilityProviderInfo, \
    Unit, Meter, MeterRead, MeterError, NewAccountFee, LateFee, AdminFee, \
    RecollectionFee
from core.models.utilityprovider import Utility, Location, UtilityProvider, \
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
        property_str = "Property: " + name + ", Zip Code:" + \
                       str(zip_code)
        self.assertEqual(property_.name, name)
        self.assertEqual(property_.street_address, street_address)
        self.assertEqual(property_.zip_code, zip_code)
        self.assertEqual(property_.attribute, attribute)
        self.assertEqual(str(property_), property_str)

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
        unit_str = "Unit: " + unit_name + \
                   ", Property: " + str(property_.name)
        self.assertEqual(unit.property, property_)
        self.assertEqual(unit.name, unit_name)
        self.assertEqual(str(unit), unit_str)

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
        installed_date = timezone.now()
        uninstalled_date = timezone.now()
        meter = Meter.objects.create(
            name=meter_name,
            utility=self.utility,
            unit=unit,
            installed_date=installed_date,
            uninstalled_date=uninstalled_date
        )
        meter_str = "Meter: " + meter_name + ", Utility: "\
                    + str(self.utility) + ", Unit: " + str(unit.name)
        self.assertEqual(meter.unit, unit)
        self.assertEqual(meter.name, meter_name)
        self.assertEqual(meter.installed_date, installed_date)
        self.assertEqual(meter.uninstalled_date, uninstalled_date)
        self.assertEqual(str(meter), meter_str)

    def test_create_propertyutilityproviderinfo_create(self):
        """ Test to create PropertyUtilityProviderInfo"""
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
        property_utility_provider_info = PropertyUtilityProviderInfo.objects.create(
            utility_provider=utility_provider,
            property=property_,
            allowance_units=allowance_units,
            bill_period_day=bill_period_day,
            bill_post_day=bill_post_day,
            default_usage=default_usage
        )
        self.assertEqual(property_utility_provider_info.utility_provider,
                         utility_provider)
        self.assertEqual(property_utility_provider_info.property, property_)
        self.assertEqual(property_utility_provider_info.allowance_units,
                         allowance_units)
        self.assertEqual(property_utility_provider_info.bill_period_day,
                         bill_period_day)
        self.assertEqual(property_utility_provider_info.bill_post_day,
                         bill_post_day)
        self.assertEqual(property_utility_provider_info.default_usage,
                         default_usage)

    def test_create_meter_read_str(self):
        """Test to create meter read object and custom str method"""
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        unit = Unit.objects.create(name="Unit Test",
                                   property=property_)
        meter_name = "Meter Test"
        meter = Meter.objects.create(
            name=meter_name,
            utility=self.utility,
            unit=unit,
            installed_date=timezone.now(),
            uninstalled_date=timezone.now()
        )
        read_dt = timezone.now()
        amount = 992
        meter_read = MeterRead.objects.create(meter=meter,
                                              read_date=read_dt,
                                              amount=amount)
        meter_str = "Meter: " + meter_name + ", Read Date: " + \
                    str(read_dt) + ", Amount: " + str(amount)
        self.assertEqual(meter_read.read_date, read_dt)
        self.assertEqual(meter_read.amount, amount)
        self.assertEqual(meter_read.meter.name, meter_name)
        self.assertEqual(str(meter_read), meter_str)

    def test_create_meter_error_str(self):
        """Test to create meter error object and custom str method"""
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        unit = Unit.objects.create(name="Unit Test",
                                   property=property_)
        meter_name = "Meter Test"
        meter = Meter.objects.create(
            name=meter_name,
            utility=self.utility,
            unit=unit,
            installed_date=timezone.now(),
            uninstalled_date=timezone.now()
        )
        error_dt = repair_dt = timezone.now()
        desc = "Sample description."
        meter_error = MeterError.objects.create(meter=meter,
                                                error_date=error_dt,
                                                description=desc,
                                                repair_date=repair_dt)

        error_str = "Meter: " + meter_name + ", Error Date: " + \
                    str(error_dt) + ", Description: " + \
                    str(desc)
        self.assertEqual(meter_error.error_date, error_dt)
        self.assertEqual(meter_error.repair_date, repair_dt)
        self.assertEqual(meter_error.description, desc)
        self.assertEqual(meter_error.meter.name, meter_name)
        self.assertEqual(str(meter_error), error_str)

    def test_create_new_acc_fee_str(self):
        """ Test to create new acc fee object and custom str method """
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        name = "New Acc Fee 1"
        amount, priority = 8, 2
        new_acc_fee_obj = NewAccountFee.objects.create(
            name=name,
            amount=amount,
            property=property_,
            priority=priority
        )
        self.assertEqual(new_acc_fee_obj.name, name)
        self.assertEqual(new_acc_fee_obj.property, property_)
        self.assertEqual(new_acc_fee_obj.amount, amount)
        self.assertEqual(new_acc_fee_obj.priority, priority)
        self.assertEqual(str(new_acc_fee_obj), name)

    def test_create_late_fee_str(self):
        """ Test to create late fee object and custom str method """
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        name = "New Acc Fee 1"
        amount, days_late, priority = 89, 2, 1
        late_fee_obj = LateFee.objects.create(
            name=name,
            amount=amount,
            property=property_,
            days_late=days_late,
            priority=priority
        )
        self.assertEqual(late_fee_obj.name, name)
        self.assertEqual(late_fee_obj.property, property_)
        self.assertEqual(late_fee_obj.amount, amount)
        self.assertEqual(late_fee_obj.priority, priority)
        self.assertEqual(late_fee_obj.days_late, days_late)
        self.assertEqual(str(late_fee_obj), name)

    def test_create_admin_fee_str(self):
        """ Test to create admin fee object and custom str method """
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        name = "New Acc Fee 1"
        amount, priority = 89, 1
        admin_fee_obj = AdminFee.objects.create(
            name=name,
            amount=amount,
            property=property_,
            priority=priority
        )
        self.assertEqual(admin_fee_obj.name, name)
        self.assertEqual(admin_fee_obj.property, property_)
        self.assertEqual(admin_fee_obj.amount, amount)
        self.assertEqual(admin_fee_obj.priority, priority)
        self.assertEqual(str(admin_fee_obj), name)

    def test_create_rec_fee_str(self):
        """ Test to create Recollection Fee object and custom str method"""
        property_ = Property.objects.create(
            name="Property Test",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        name = "New Acc Fee 1"
        amount, priority, split_value = 89, 1, True
        rec_fee_obj = RecollectionFee.objects.create(
            name=name,
            amount=amount,
            usage_based_split=split_value,
            property=property_,
            priority=priority
        )
        self.assertEqual(rec_fee_obj.name, name)
        self.assertEqual(rec_fee_obj.property, property_)
        self.assertEqual(rec_fee_obj.amount, amount)
        self.assertEqual(rec_fee_obj.priority, priority)
        self.assertEqual(rec_fee_obj.usage_based_split, split_value)
        self.assertEqual(str(rec_fee_obj), name)
