from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models.utilityprovider import Utility, Provider, UtilityProvider
from .serializers import UtilitySerializer, \
    ProviderSerializer, UtilityProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny, ]


class UtilityProviderViewSet(viewsets.ModelViewSet):
    queryset = UtilityProvider.objects.all()
    serializer_class = UtilityProviderSerializer
    permission_classes = [permissions.AllowAny, ]


class ListUtilities(APIView):
    def get(self, request):
        utilities = Utility.objects.all()
        serializer = UtilitySerializer(utilities, many=True)
        return Response(serializer.data)
