from rest_framework import viewsets, permissions

from core.models.property import Meter, Property, Unit, MeterRead,\
    MeterError
from property.serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer, MeterReadSerializer,\
    MeterErrorSerializer, MeterWithLastReadSerializer

import property.services as services


# Create your views here.
class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    permission_classes = [permissions.AllowAny, ]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny, ]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.AllowAny, ]


class MeterReadViewSet(viewsets.ModelViewSet):
    queryset = MeterRead.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterReadSerializer


class MeterErrorViewSet(viewsets.ModelViewSet):
    queryset = MeterError.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterErrorSerializer


# custom views here
class ListUnitsForProperty(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UnitSerializer

    def get_queryset(self):
        property_id = self.kwargs['id']
        queryset = services.get_units_for_property(property_id)
        return queryset


class ListMetersForUnit(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterWithLastReadSerializer

    def get_queryset(self):
        unit_id = self.kwargs['id']
        queryset = services.get_meters_for_unit(unit_id)
        return queryset


class ListMeterReadsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterReadSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        queryset = services.get_meter_reads_for_meter(meter_id)
        return queryset


class ListMeterErrorsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterErrorSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        queryset = services.get_meter_errors_for_meter(meter_id)
        return queryset
