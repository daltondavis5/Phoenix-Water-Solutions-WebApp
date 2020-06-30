from rest_framework import viewsets, permissions

from core.models.property import Meter, Property, Unit, MeterRead
from .serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer, MeterReadSerializer


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


class ListUnitsForProperty(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UnitSerializer

    def get_queryset(self):
        property_id = self.kwargs['id']
        return Unit.objects.filter(property=property_id)


class MeterReadViewSet(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterReadSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        return MeterRead.objects.filter(meter=meter_id)
