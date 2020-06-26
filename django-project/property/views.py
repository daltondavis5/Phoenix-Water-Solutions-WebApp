from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models.property import Meter, Property, Unit
from property.serializers.property import MeterViewSerializer, \
    PropertyViewSerializer, UnitViewSerializer


# Create your views here.
class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterViewSerializer
    permission_classes = [permissions.AllowAny, ]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertyViewSerializer
    permission_classes = [permissions.AllowAny, ]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitViewSerializer
    permission_classes = [permissions.AllowAny, ]
