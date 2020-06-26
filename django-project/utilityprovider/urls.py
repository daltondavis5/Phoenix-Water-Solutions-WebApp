from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ListUtilities, UtilityProviderViewSet

router = DefaultRouter()
router.register('provider', ProviderViewSet)
router.register('utilityprovider', UtilityProviderViewSet)

urlpatterns = [
    path('utility/', ListUtilities.as_view(), name='utility-list'),
    path('', include(router.urls))
]
