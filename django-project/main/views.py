from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models.utilityprovider import Utility, Provider
from main.serializers.utilityprovider import UtilitySerializer, \
    ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.AllowAny, ]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.save()
        return Response({
            "provider": ProviderSerializer(provider,
                        context=self.get_serializer_context()).data
        })


class ListUtilities(APIView):

    def get(self, request):
        utilities = Utility.objects.all()
        serializer = UtilitySerializer(utilities, many=True)
        return Response({"utilities": serializer.data})
