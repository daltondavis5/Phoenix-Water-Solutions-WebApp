from rest_framework import viewsets, permissions

from core.models.tenant import Tenant, TenantCharge,\
    Payment, PaymentMethod
from tenant.serializers import TenantSerializer, TenantUsageSerializer,\
    TenantChargeSerializer, PaymentSerializer, PaymentMethodSerializer

import tenant.services as services


# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.AllowAny, ]


class TenantChargeViewSet(viewsets.ModelViewSet):
    queryset = TenantCharge.objects.all()
    serializer_class = TenantChargeSerializer
    permission_classes = [permissions.AllowAny, ]


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['get', 'post', 'delete']


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.AllowAny, ]


# Create custom views here.
class ListTenantsForUnit(viewsets.generics.ListAPIView):
    serializer_class = TenantUsageSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        unit_id = self.kwargs['id']
        queryset = services.get_tenants_for_unit(unit_id)
        return queryset


class ListChargesForTenant(viewsets.generics.ListAPIView):
    serializer_class = TenantChargeSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        tenant_id = self.kwargs['id']
        queryset = services.get_charges_for_tenant(tenant_id)

        return queryset


class ListPaymentsForTenant(viewsets.generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        tenant_id = self.kwargs['id']
        queryset = services.get_payments_for_tenant(tenant_id)
        return queryset
