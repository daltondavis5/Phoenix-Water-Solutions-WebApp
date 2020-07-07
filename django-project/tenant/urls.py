from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tenant.views import TenantViewSet, ListTenantsForUnit

router = DefaultRouter()
router.register('tenant', TenantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('unit/<int:id>/tenants', ListTenantsForUnit.as_view(),
         name='unit-tenants-list'),
]
