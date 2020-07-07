from django.test import TestCase

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.tenant import Tenant, TenantCharge, \
    PaymentMethod, Payment, TenantChargePayment, TenantNotes
from core.models.property import Unit, Property
from django.utils import timezone


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

        self.property = Property.objects.create(
            name="Property Test 1",
            street_address="9999 Test Paradise",
            attribute=False,
            zip_code=99999
        )
        self.unit = Unit.objects.create(name="unit 1", property=self.property)

    def test_create_tenant_and_str(self):
        """ Test to create tenant model """
        account_number = "0123456789"
        first_name = "firstname"
        last_name = "lastname"
        email = "test@pws.com"
        sec_email = "test2@pws.com"
        primary_phone = "9999999999"
        secondary_phone = "8888888888"
        unit = self.unit
        move_in_date = "2020-01-01"
        move_out_date = "2021-01-01"
        credits = 99.5
        late_fee_exemption = "2020-01-31"

        tenant = Tenant.objects.create(
            account_number=account_number,
            first_name=first_name,
            last_name=last_name,
            primary_email=email,
            secondary_email=sec_email,
            primary_phone_number=primary_phone,
            secondary_phone_number=secondary_phone,
            unit=unit,
            move_in_date=move_in_date,
            move_out_date=move_out_date,
            credits=credits,
            late_fee_exemption=late_fee_exemption
        )

        tenant_str = "Tenant Name:" + first_name + ", Primary Email:" + \
            email + ", Unit:" + str(self.unit.name)

        self.assertEqual(account_number, tenant.account_number)
        self.assertEqual(first_name, tenant.first_name)
        self.assertEqual(last_name, tenant.last_name)
        self.assertEqual(email, tenant.primary_email)
        self.assertEqual(primary_phone, tenant.primary_phone_number)
        self.assertEqual(secondary_phone, tenant.secondary_phone_number)
        self.assertEqual(unit, tenant.unit)
        self.assertEqual(move_out_date, tenant.move_out_date)
        self.assertEqual(move_in_date, tenant.move_in_date)
        self.assertEqual(credits, tenant.credits)
        self.assertEqual(late_fee_exemption, tenant.late_fee_exemption)
        self.assertEqual(str(tenant), tenant_str)

    def test_create_tenant_charge_and_str(self):
        """ Test to create a tenant charge model and test str"""
        first_name = "firstname"
        phone = "9999999999"
        tenant = Tenant.objects.create(
            account_number="0123456789",
            first_name=first_name,
            last_name="lastname",
            primary_email="test@pws.com",
            primary_phone_number=phone,
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
        )
        initial_amount = 999.50
        remaining_amount = 100.50
        description = "Test Desc"
        bill_period_end_date = "2020-12-31"
        due_date = "2020-01-31"
        priority = 2
        created = timezone.now()
        batch_id = 1

        tenant_charge = TenantCharge.objects.create(
            tenant=tenant,
            initial_amount=initial_amount,
            remaining_amount=remaining_amount,
            description=description,
            bill_period_end_date=bill_period_end_date,
            due_date=due_date,
            priority=priority,
            created=created,
            batch_id=batch_id
        )
        tenant_charge_str = "Tenant: " + first_name + ", Due Date: " + \
                            due_date + ", Initial Amount: " + \
                            str(initial_amount) + ", Remaining Amount: " + \
                            str(remaining_amount)

        self.assertEqual(tenant_charge.tenant, tenant)
        self.assertEqual(tenant_charge.initial_amount, initial_amount)
        self.assertEqual(tenant_charge.remaining_amount, remaining_amount),
        self.assertEqual(tenant_charge.description, description)
        self.assertEqual(tenant_charge.due_date, due_date)
        self.assertEqual(tenant_charge.priority, priority)
        self.assertEqual(tenant_charge.created, created)
        self.assertEqual(tenant_charge.batch_id, batch_id)
        self.assertEqual(tenant_charge_str, str(tenant_charge))

    def test_create_payment_method_model(self):
        """ Test to create payment method model """
        name = "Test Payment Method"
        method = PaymentMethod.objects.create(
            name=name
        )
        method_str = "Payment Method: " + name
        self.assertEqual(method_str, str(method))

    def test_create_payment_model_and_str(self):
        """ Test to create payment model and str """
        tenant = Tenant.objects.create(
            account_number="0123456789",
            first_name="firstname",
            last_name="lastname",
            primary_email="test@pws.com",
            primary_phone_number="9999999999",
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
        )
        method = PaymentMethod.objects.create(
            name="Test Payment Method"
        )
        payment_date = "2020-07-31"
        payment_amount = 999.50
        applied_amount = 300.00
        payment_method = method

        payment = Payment.objects.create(
            tenant=tenant,
            payment_date=payment_date,
            payment_amount=payment_amount,
            applied_amount=applied_amount,
            payment_method=payment_method,
        )
        payment_str = "Tenant: " + "firstname" + ", Payment Amount: " \
                      + str(payment_amount) + ", Payment Date:  " + \
                      payment_date

        self.assertEqual(payment.tenant, tenant)
        self.assertEqual(payment.payment_date, payment_date)
        self.assertEqual(payment.payment_amount, payment_amount)
        self.assertEqual(payment.applied_amount, applied_amount)
        self.assertEqual(payment.payment_method, payment_method)
        self.assertEqual(str(payment), payment_str)

    def test_payment_tenant_charge_create(self):
        """ Test to create PaymentTenantCharge model and
        reverse relationship. """
        tenant = Tenant.objects.create(
            account_number="0123456789",
            first_name="firstname",
            last_name="lastname",
            primary_email="test@pws.com",
            primary_phone_number="9999999999",
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
        )
        tenant_charge = TenantCharge.objects.create(
            tenant=tenant,
            initial_amount=999.50,
            remaining_amount=100.50,
            description="Test Desc",
            bill_period_end_date="2020-12-31",
            due_date="2020-01-31",
            priority=2,
            created=timezone.now(),
            batch_id=1
        )
        name = "Test Payment Method"
        method = PaymentMethod.objects.create(
            name=name
        )
        payment = Payment.objects.create(
            tenant=tenant,
            payment_date="2020-07-31",
            payment_amount=999.50,
            applied_amount=300.00,
            payment_method=method
        )
        payment_tenant_charge = TenantChargePayment.objects.create(
            payment=payment,
            tenant_charge=tenant_charge
        )
        self.assertEqual(payment_tenant_charge.payment, payment)
        self.assertEqual(payment_tenant_charge.tenant_charge, tenant_charge)
        self.assertEqual(str(payment.charges_applied_to.all()[0]),
                         str(tenant_charge))
        self.assertEqual(str(tenant_charge.payment_set.all()[0]),
                         str(payment))

    def test_create_tenant_notes(self):
        """ Test to create tenant notes model """
        tenant = Tenant.objects.create(
            account_number="0123456789",
            first_name="firstname",
            last_name="lastname",
            primary_email="test@pws.com",
            primary_phone_number="9999999999",
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
        )
        date_logged = "2020-01-01"
        tenant_notes = TenantNotes.objects.create(
            tenant=tenant,
            date_logged=date_logged,
            note="Test Note"
        )
        tenant_notes_str = "Tenant: " + tenant.first_name + \
                           " ,Date Logged:" + date_logged
        self.assertEqual(str(tenant_notes), tenant_notes_str)
