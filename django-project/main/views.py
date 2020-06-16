from rest_framework import viewsets, permissions
from rest_framework.response import Response
from core.models.utilityprovider import UtilityProvider, Utility
from .serializers import UtilityProviderSerializer, UtilitySerializer


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
