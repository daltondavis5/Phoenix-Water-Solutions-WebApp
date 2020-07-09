from rest_framework import viewsets, permissions
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import services
from core.models.property import Meter, Property, Unit, MeterRead,\
    MeterError
from .serializers import MeterSerializer, \
    PropertySerializer, UnitSerializer, MeterReadSerializer,\
    MeterErrorSerializer, MeterWithLastReadSerializer, PropertyMeterReadSerializer
import io
from rest_framework.parsers import JSONParser


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
#     permission_classes = [permListMeterreadsForMeterissions.AllowAny, ]
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


@api_view(["POST"])
def get_property_utility_usage_amount(request):
    """API to calculate meter usage amount for all Units in a Property"""
    if request.method == "POST":
        serializer = PropertyMeterReadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pid = serializer.validated_data.get("property_id")
            from_date = serializer.validated_data.get("from_date")
            to_date = serializer.validated_data.get("to_date")
            utility_type = serializer.validated_data.get("utility_type")

            resp = services.get_utility_usage_amount_for_property(
                pid, from_date, to_date, utility_type)
            return Response(data=resp, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ListMeterErrorsForMeter(viewsets.generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MeterErrorSerializer

    def get_queryset(self):
        meter_id = self.kwargs['id']
        return MeterError.objects.filter(meter=meter_id)
