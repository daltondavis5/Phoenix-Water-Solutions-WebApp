from rest_framework import viewsets, permissions

from core.models.property import Meter, Property, Unit, MeterRead,\
    MeterError
from .serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer, MeterReadSerializer,\
    MeterErrorSerializer, MeterWithLastReadSerializer


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


# class MeterReadViewSet(viewsets.ModelViewSet):
#     queryset = MeterRead.objects.all()
#     permission_classes = [permissions.AllowAny, ]
#     serializer_class = MeterReadSerializer
#
#
# class MeterErrorViewSet(viewsets.ModelViewSet):
#     queryset = MeterError.objects.all()
#     permission_classes = [permissions.AllowAny, ]
#     serializer_class = MeterErrorSerializer


# custom views here
class ListUnitsForProperty(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UnitSerializer

    def get_queryset(self):
        property_id = self.kwargs['id']
        return Unit.objects.filter(property=property_id)


class ListMetersForUnit(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterWithLastReadSerializer

    def get_queryset(self):
        unit_id = self.kwargs['id']
        return Meter.objects.filter(unit=unit_id)


class ListMeterReadsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterReadSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        return MeterRead.objects.filter(meter=meter_id)


class ListMeterErrorsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterErrorSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        return MeterError.objects.filter(meter=meter_id)
