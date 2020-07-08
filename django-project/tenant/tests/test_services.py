from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Property
from core.models.tenant import Tenant, TenantCharge
from django.utils import timezone
import tenant.services as services
from rest_framework.test import APITestCase


class TenantServicesTestCase(APITestCase):

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
            remaining_amount=20,
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
            remaining_amount=25,
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
            remaining_amount=100.50,
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
            remaining_amount=100.50,
            description="Test Desc",
            bill_period_end_date=timezone.now().date() +
                                 timezone.timedelta(days=30),
            due_date=timezone.now().date() + timezone.timedelta(days=30),
            priority=2,
            created=timezone.now(),
            batch_id=1,
        )

    def test_get_tenants_for_unit(self):
        """ Test to get all tenant for a unit """
        unit_id = self.unit.id
        actual = services.get_tenants_for_unit(unit_id)
        actual = [str(actual[0]), str(actual[1])]
        self.assertIn(str(self.tenant1), actual)
        self.assertIn(str(self.tenant2), actual)

    def test_fail_get_tenants_for_unit(self):
        """ Test case to fail get all tenants for a unit """
        unit_id1 = 0
        unit_id2 = "s"
        queryset1 = services.get_tenants_for_unit(unit_id1)
        queryset2 = services.get_tenants_for_unit(unit_id2)

        self.assertEqual(len(queryset1), 0)
        self.assertFalse(queryset2)

    def test_get_current_balance_for_tenant(self):
        """ Test case to get current balance for a tenant """
        curr_bal1 = 45.0
        tenant_id1 = self.tenant1.id
        curr_bal2 = 201.0
        tenant_id2 = self.tenant2.id
        self.assertEqual(curr_bal1,
                         services.get_current_balance_for_tenant(tenant_id1))
        self.assertEqual(curr_bal2,
                         services.get_current_balance_for_tenant(tenant_id2))

    def test_fail_get_current_balance_for_tenant(self):
        """ Test case to fail get current balance for tenant"""
        tenant_id1 = 0
        tenant_id2 = "s"
        self.assertEqual(services.get_current_balance_for_tenant(tenant_id1),
                         0.0)
        self.assertEqual(services.get_current_balance_for_tenant(tenant_id2),
                         0.0)

    def test_get_overdue_balance_for_tenant(self):
        """ Test case to get overdue balance for a tenant """
        overdue_bal1 = 25.0
        overdue_bal2 = 0.0
        tenant_id1 = self.tenant1.id
        tenant_id2 = self.tenant2.id
        self.assertEqual(overdue_bal1,
                         services.get_overdue_balance_for_tenant(tenant_id1))
        self.assertEqual(overdue_bal2,
                         services.get_overdue_balance_for_tenant(tenant_id2))

    def test_fail_get_overdue_balance_for_tenant(self):
        """ Test case to fail get overdue balance for tenant"""
        tenant_id1 = 0
        tenant_id2 = "s"
        self.assertEqual(services.get_overdue_balance_for_tenant(tenant_id1),
                         0.0)
        self.assertEqual(services.get_overdue_balance_for_tenant(tenant_id2),
                         0.0)

    def test_get_tenant_usage_info(self):
        """ Test case to get tenant usage info """
        overdue_bal1 = 25.0
        overdue_bal2 = 0.0
        curr_bal1 = 45.0
        curr_bal2 = 201.0
        tenant_id1 = self.tenant1.id
        tenant_id2 = self.tenant2.id
        usage1 = ["current_balance:" + str(curr_bal1),
                  "overdue_balance:" + str(overdue_bal1)]
        usage2 = ["current_balance:" + str(curr_bal2),
                  "overdue_balance:" + str(overdue_bal2)]
        self.assertEqual(services.get_tenant_usage_info(tenant_id1),
                         usage1)
        self.assertEqual(services.get_tenant_usage_info(tenant_id2),
                         usage2)

    def test_fail_get_tenant_usage_info(self):
        """ Test case to fail get tenant usage info """
        tenant_id1 = 0
        tenant_id2 = "s"
        usage1 = ["current_balance:" + str(0.0),
                  "overdue_balance:" + str(0.0)]
        self.assertEqual(services.get_tenant_usage_info(tenant_id1),
                         usage1)
        self.assertEqual(services.get_tenant_usage_info(tenant_id2),
                         usage1)
