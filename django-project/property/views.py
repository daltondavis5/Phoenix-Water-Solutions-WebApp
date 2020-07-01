from rest_framework import viewsets, permissions
from rest_framework import status

import datetime
from core.models.property import Meter, Property, Unit, MeterRead
from .serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer, MeterReadSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import PropertyService as PS


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


class ListMetersForUnit(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterSerializer

    def get_queryset(self):
        unit_id = self.kwargs['id']
        return Meter.objects.filter(unit=unit_id)


class ListMeterreadsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterReadSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        return MeterRead.objects.filter(meter=meter_id)


@api_view(['POST'])
def get_property_amount(request):
    """API to calculate meter amount for all Units in a Property"""
    if request.method == "POST":

        pid = request.data.get('property_id')
        from_date = datetime.datetime.strptime(request.data.get('from_date')
                                               , "%Y-%m-%d").date()
        to_date = datetime.datetime.strptime(request.data.get('to_date')
                                             , "%Y-%m-%d").date()
        utility_id = request.data.get('utility_id')



        if from_date > to_date:
            return Response("To date can't me greater than from date",
                            status=status.HTTP_404_NOT_FOUND)
        amount = PS.get_property_amount(pid, utility_id, from_date, to_date)
        return Response({"total_amount": amount})
