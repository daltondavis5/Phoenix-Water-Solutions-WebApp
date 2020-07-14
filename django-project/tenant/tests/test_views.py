from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Property
from core.models.tenant import Tenant, TenantCharge, Payment, PaymentMethod
from tenant.serializers import TenantChargeInfoSerializer, \
    TenantChargeSerializer, PaymentSerializer
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


def get_reverse_url_payment_list():
    return reverse('payment-list')


def get_reverse_url_tenant_charge_list():
    return reverse('tenantcharge-list')


def detail_url_tenant(tenant_id):
    return reverse("tenant-detail", args=[tenant_id])


def get_reverse_url_unit_tenant_list(unit_id):
    return reverse("unit-tenants-list", args=[unit_id])


def get_reverse_url_tenant_charges_list(tenant_id):
    return reverse("tenant-charges-list", args=[tenant_id])


def get_reverse_url_tenant_payment_list(tenant_id):
    return reverse("tenant-payment-list", args=[tenant_id])


def get_reverse_url_payment_detail(payment_id):
    return reverse("payment-detail", args=[payment_id])


# Create your tests here.

class TenantViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.utility = Utility.objects.create(type='Water')
        self.location = Location.objects.create(city='Phoenix',
                                                state='AZ')
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
        self.unit = Unit.objects.create(name="unit 1",
                                        property=self.property)
        self.tenant1 = Tenant.objects.create(
            account_number="1",
            first_name="test first name",
            last_name="test last name",
            primary_email="test@pws.com",
            secondary_email="test2@pws.com",
            primary_phone_number="9999999999",
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date=timezone.now().date() -
            timezone.timedelta(days=1),
            move_out_date=timezone.now().date() +
                          timezone.timedelta(days=365),
            credits=99.5,
            late_fee_exemption=timezone.now().date() +
            timezone.timedelta(days=15),
        )
        self.tenant2 = Tenant.objects.create(
            account_number="2",
            first_name="test second",
            last_name="test second name",
            primary_email="test3@pws.com",
            secondary_email="test4@pws.com",
            primary_phone_number="9999999990",
            secondary_phone_number="8888888880",
            unit=self.unit,
            move_in_date=timezone.now().date() - timezone.timedelta(days=1),
            move_out_date=timezone.now().date() + timezone.timedelta(days=365),
            credits=99.5,
            late_fee_exemption=timezone.now().date() +
            timezone.timedelta(days=15),
        )
        self.tenant_charge1 = TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=100,
            description="Test Desc",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() + timezone.timedelta(days=5),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )
        self.tenant_charge2 = TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=100,
            description="Test Desc",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() - timezone.timedelta(days=1),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )
        self.tenant_charge3 = TenantCharge.objects.create(
            tenant=self.tenant2,
            initial_amount=999.50,
            description="Test Desc",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() +
            timezone.timedelta(days=30),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

        self.tenant_charge4 = TenantCharge.objects.create(
            tenant=self.tenant2,
            initial_amount=999.50,
            description="Test Desc",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() + timezone.timedelta(days=30),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

        self.payment_method = PaymentMethod.objects.create(name="Card")

        self.payment1 = Payment.objects.create(
            tenant=self.tenant1,
            payment_date=timezone.now().date(),
            payment_amount=100,
            payment_method=self.payment_method,
        )

        self.payment2 = Payment.objects.create(
            tenant=self.tenant2,
            payment_date=timezone.now().date(),
            payment_amount=50,
            payment_method=self.payment_method,
        )

    def test_tenant_update_move_in_date(self):
        """ Test to not allow to update move in date """
        tenant = self.tenant1
        payload = {
            "account_number": "0123456789",
            "first_name": "test first name",
            "last_name": "test last name",
            "primary_email": "test@pws.com",
            "secondary_email": "test2@pws.com",
            "primary_phone_number": "9999999999",
            "secondary_phone_number": "8888888888",
            "move_in_date": timezone.now().date() - timezone.timedelta(days=2),
            "move_out_date": timezone.now().date() +
                             timezone.timedelta(days=365),
            "credits": 0,
            "late_fee_exemption": timezone.now().date() +
            timezone.timedelta(days=15),
            "unit": self.unit.id
        }
        url = detail_url_tenant(tenant.id)
        response = self.client.put(url, payload)
        tenant.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_tenant_update_move_out_date(self):
        """ Test to verify that move in date is less than move out date """
        tenant = self.tenant1
        payload = {
            "account_number": "0123456789",
            "first_name": "test first name",
            "last_name": "test last name",
            "primary_email": "test@pws.com",
            "secondary_email": "test2@pws.com",
            "primary_phone_number": "9999999999",
            "secondary_phone_number": "8888888888",
            "move_in_date": timezone.now().date() - timezone.timedelta(days=1),
            "move_out_date": timezone.now().date() -
                             timezone.timedelta(days=365),
            "credits": 0,
            "late_fee_exemption": timezone.now().date() +
            timezone.timedelta(days=15),
            "unit": self.unit.id
        }
        url = detail_url_tenant(tenant.id)
        response = self.client.put(url, payload)
        tenant.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_tenant_get_info(self):
        """ Test to retrieve all the info of a tenant including
        tenant usage info from tenant charge table """
        serializer1 = TenantChargeInfoSerializer(self.tenant1)

        url = get_reverse_url_unit_tenant_list(self.unit.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(serializer1.data, response.data)

    def test_tenant_charges_list_for_tenant(self):
        """ Test to retrieve all charges for a given tenant """

        serializer1 = TenantChargeSerializer(self.tenant_charge1)
        serializer2 = TenantChargeSerializer(self.tenant_charge2)

        serializer3 = TenantChargeSerializer(self.tenant_charge3)
        serializer4 = TenantChargeSerializer(self.tenant_charge4)

        url = get_reverse_url_tenant_charges_list(self.tenant1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn(serializer1.data, response.data)
        self.assertIn(serializer2.data, response.data)
        self.assertNotIn(serializer3.data, response.data)
        self.assertNotIn(serializer4.data, response.data)

    def test_tenant_payment_list_for_tenant(self):
        """Test retrieve all payments of a tenant"""

        serializer1 = PaymentSerializer(self.payment1)
        serializer2 = PaymentSerializer(self.payment2)

        url = get_reverse_url_tenant_payment_list(self.tenant1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn(serializer1.data, response.data)
        self.assertNotIn(serializer2.data, response.data)

    def test_put_not_allowed_payment(self):
        """Test payment update is disabled"""
        url = get_reverse_url_payment_detail(self.payment1.id)
        response = self.client.put(url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class PaymentTenantChargeTest(APITestCase):

    def setUp(self) -> None:
        self.utility = Utility.objects.create(type='Water')
        self.location = Location.objects.create(city='Phoenix',
                                                state='AZ')
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

        self.unit = Unit.objects.create(name="unit 1",
                                        property=self.property)

        self.tenant1 = Tenant.objects.create(
            account_number="1",
            first_name="test first name",
            last_name="test last name",
            primary_email="test@pws.com",
            secondary_email="test2@pws.com",
            primary_phone_number="9999999999",
            secondary_phone_number="8888888888",
            unit=self.unit,
            move_in_date=timezone.now().date() -
            timezone.timedelta(days=1),
            move_out_date=timezone.now().date() +
                          timezone.timedelta(days=365),
            credits=99.5,
            late_fee_exemption=timezone.now().date() +
            timezone.timedelta(days=15),
        )

        self.payment_method = PaymentMethod.objects.create(name="Card")

    def test_payment_charge_created(self):
        charge1_payload = {
            'tenant': self.tenant1.id,
            'initial_amount': 100.0,
            'description': "C1",
            'bill_period_end_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'due_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'priority': 2,
            'created': timezone.now(),
            'batch_id': 1,
        }
        charge1_response = self.client.post(
            get_reverse_url_tenant_charge_list(), charge1_payload)

        charge1 = TenantCharge.objects.get(id=charge1_response.data['id'])
        charge1.refresh_from_db()

        self.assertEqual(len(charge1.payment_set.all()), 0)

        payment1_payload = {
            'tenant': self.tenant1.id,
            'payment_date': timezone.now().date(),
            'payment_amount': 50.0,
            'payment_method': self.payment_method.name,
        }

        payment1_response = self.client.post(
            get_reverse_url_payment_list(), payment1_payload)
        payment1 = Payment.objects.get(id=payment1_response.data['id'])
        payment1.refresh_from_db()
        self.assertEqual(payment1.charges_applied_to.all()[
                         0].id, charge1.id)
        self.assertEqual(charge1.payment_set.all()[
                         0].id, payment1_response.data['id'])

        payment2_payload = {
            'tenant': self.tenant1.id,
            'payment_date': timezone.now().date(),
            'payment_amount': 150.0,
            'payment_method': self.payment_method.name,
        }

        payment2_response = self.client.post(
            get_reverse_url_payment_list(), payment2_payload)
        payment2 = Payment.objects.get(id=payment2_response.data['id'])
        payment2.refresh_from_db()
        self.assertEqual(payment2.charges_applied_to.all()[
                         0].id, charge1_response.data['id'])
        self.assertEqual(charge1.payment_set.all()[
                         1].id, payment2_response.data['id'])

        charge2_payload = {
            'tenant': self.tenant1.id,
            'initial_amount': 20.0,
            'description': "C1",
            'bill_period_end_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'due_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'priority': 2,
            'created': timezone.now(),
            'batch_id': 1,
        }
        charge2_response = self.client.post(
            get_reverse_url_tenant_charge_list(), charge2_payload)
        charge2 = TenantCharge.objects.get(id=charge2_response.data['id'])
        charge2.refresh_from_db()

        self.assertEqual(len(charge2.payment_set.all()), 1)
        self.assertEqual(payment2.charges_applied_to.all()[
                         1].id, charge2_response.data['id'])
        self.assertEqual(charge2.payment_set.all()[
                         0].id, payment2_response.data['id'])

        charge3_payload = {
            'tenant': self.tenant1.id,
            'initial_amount': 100.0,
            'description': "C1",
            'bill_period_end_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'due_date': timezone.now().date() +
            timezone.timedelta(days=30),
            'priority': 2,
            'created': timezone.now(),
            'batch_id': 1,
        }
        charge3_response = self.client.post(
            get_reverse_url_tenant_charge_list(), charge3_payload)
        charge3 = TenantCharge.objects.get(id=charge2_response.data['id'])
        self.assertEqual(len(charge3.payment_set.all()), 1)
        self.assertEqual(payment2.charges_applied_to.all()[
                         2].id, charge3_response.data['id'])
        self.assertEqual(charge3.payment_set.all()[
                         0].id, payment2_response.data['id'])

    def test_get_current_balance_and_overdue_balance_for_tenant(self):
        """ Test case to get current balance and overdue balance
         for a tenant """
        TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=100.0,
            description="C1",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() +
            timezone.timedelta(days=30),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

        TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=50.0,
            description="C2",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() +
            timezone.timedelta(days=30),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

        TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=40.0,
            description="C3-due",
            bill_period_end_date=timezone.now().date() +
            timezone.timedelta(days=30),
            due_date=timezone.now().date() -
            timezone.timedelta(days=2),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )
        payload = {
            'tenant': self.tenant1.id,
            'payment_date': timezone.now().date(),
            'payment_amount': 50.0,
            'payment_method': self.payment_method.name,
        }

        self.client.post(get_reverse_url_payment_list(),
                         payload)

        url = get_reverse_url_unit_tenant_list(self.unit.id)
        response = self.client.get(url)

        curr_bal = 140.0
        overdue_bal = 0.0
        self.assertEqual(curr_bal,
                         response.data[0].get('tenant_charge_info').
                         get('current_balance'))
        self.assertEqual(overdue_bal,
                         response.data[0].get('tenant_charge_info').
                         get('overdue_balance'))
