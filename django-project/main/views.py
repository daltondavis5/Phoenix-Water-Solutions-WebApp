from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models.utilityprovider import UtilityProvider, Utility, Provider
from .serializers import UtilityProviderSerializer, UtilitySerializer, ProviderSerializer


class UtilityProviderViewSet(viewsets.ModelViewSet):
    queryset = UtilityProvider.objects.all()
    serializer_class = UtilityProviderSerializer
    permission_classes = [permissions.AllowAny, ]


"""     def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        utilityprovider = serializer.save()
        return Response({
            "utilityprovider": UtilityProviderSerializer(utilityprovider, context=self.get_serializer_context()).data
        }) """


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny, ]

    def create(self, request):
        # print("Request: " + request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.save()
        return Response({
            "provider": ProviderSerializer(provider, context=self.get_serializer_context()).data
        })
