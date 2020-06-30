from django.urls import path, include
from rest_framework.routers import DefaultRouter
from property.views import MeterViewSet, PropertyViewSet, UnitViewSet,\
    ListUnitsForProperty, MeterReadViewSet

router = DefaultRouter()
router.register('property', PropertyViewSet)
router.register('meter', MeterViewSet)
router.register('unit', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('property/<int:id>/units', ListUnitsForProperty.as_view(),
         name="unit-list"),
    path('meter/<int:id>/reads', MeterReadViewSet.as_view(),
         name='meter-list')
]
