from rest_framework import viewsets, permissions

from core.models.tenant import Tenant
from core.models.property import Unit
from property.serializers import UnitSerializer
from tenant.serializers import TenantSerializer, TenantUsageSerializer

import tenant.services as services


# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.AllowAny, ]


# Create custom views here.
class ListTenantsForUnit(viewsets.generics.ListAPIView):
    serializer_class = TenantUsageSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        unit_id = self.kwargs['id']
        queryset = services.get_tenants_for_unit(unit_id)
        return queryset
