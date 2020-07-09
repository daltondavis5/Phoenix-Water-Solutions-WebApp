from django.urls import path, include
from rest_framework.routers import DefaultRouter
from property.views import MeterViewSet, PropertyViewSet, UnitViewSet,\
    ListUnitsForProperty, ListMetersForUnit, ListMeterReadsForMeter, \
    ListMeterErrorsForMeter, get_property_utility_usage_amount


router = DefaultRouter()
router.register('property', PropertyViewSet)
router.register('meter', MeterViewSet)
router.register('unit', UnitViewSet)
# router.register('meterread', MeterReadViewSet)
# router.register('metererror', MeterErrorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('property-utility-usage-amount', get_property_utility_usage_amount,
         name="property-utility-usage-amount"),
    path('property/<int:id>/units', ListUnitsForProperty.as_view(),
         name="property-unit-list"),
    path('unit/<int:id>/meters', ListMetersForUnit.as_view(),
         name="unit-meter-list"),
    path('meter/<int:id>/reads', ListMeterReadsForMeter.as_view(),
         name='meter-meterreads-list'),
    path('meter/<int:id>/errors', ListMeterErrorsForMeter.as_view(),
         name='meter-metererrors-list'),
]
urlpatterns += router.urls
