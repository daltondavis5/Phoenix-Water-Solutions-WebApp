from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Property
from core.models.tenant import Tenant, TenantCharge
from tenant.serializers import TenantUsageSerializer
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase


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
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
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
            move_in_date="2020-01-01",
            move_out_date="2021-01-01",
            credits=99.5,
            late_fee_exemption="2020-01-31",
        )
        self.tenant_charge1 = TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=100,
            remaining_amount=20,
            description="Test Desc",
            bill_period_end_date="2020-12-31",
            due_date=timezone.now() + timezone.timedelta(days=5),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )
        self.tenant_charge2 = TenantCharge.objects.create(
            tenant=self.tenant1,
            initial_amount=100,
            remaining_amount=25,
            description="Test Desc",
            bill_period_end_date="2020-12-31",
            due_date=timezone.now() - timezone.timedelta(days=1),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )
        self.tenant_charge3 = TenantCharge.objects.create(
            tenant=self.tenant2,
            initial_amount=999.50,
            remaining_amount=100.50,
            description="Test Desc",
            bill_period_end_date="2020-12-31",
            due_date="2020-01-31",
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

        self.tenant_charge4 = TenantCharge.objects.create(
            tenant=self.tenant2,
            initial_amount=999.50,
            remaining_amount=100.50,
            description="Test Desc",
            bill_period_end_date="2020-12-31",
            due_date="2020-01-31",
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

    def detail_url_tenant(self, tenant_id):
        return reverse("tenant-detail", args=[tenant_id])

    def get_reverse_url_unit_tenant_list(self, unit_id):
        return reverse("unit-tenants-list", args=[unit_id])

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
            "move_in_date": "2020-07-07",
            "move_out_date": "2021-01-01",
            "credits": 0,
            "late_fee_exemption": "2020-01-31",
            "unit": self.unit.id
        }
        url = self.detail_url_tenant(tenant.id)
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
            "move_in_date": "2020-07-07",
            "move_out_date": "2019-01-01",
            "credits": 0,
            "late_fee_exemption": "2020-01-31",
            "unit": self.unit.id
        }
        url = self.detail_url_tenant(tenant.id)
        response = self.client.put(url, payload)
        tenant.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_tenant_get_info(self):
        """ Test to retrieve all the info of a tenant including
        tenant usage info from tenant charge table """
        serializer1 = TenantUsageSerializer(self.tenant1)

        url = self.get_reverse_url_unit_tenant_list(self.unit.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(serializer1.data, response.data)
