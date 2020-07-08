from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenant.views import TenantViewSet, ListTenantsForUnit,\
    TenantChargeViewSet, PaymentViewSet, PaymentMethodViewSet

router = DefaultRouter()
router.register('tenant', TenantViewSet)
router.register('tenantcharge', TenantChargeViewSet)
router.register('payment', PaymentViewSet)
router.register('paymentmethod', PaymentMethodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('unit/<int:id>/tenants', ListTenantsForUnit.as_view(),
         name='unit-tenants-list'),
]
