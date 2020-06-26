from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models.property import Meter, Property, Unit
from .serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer


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
