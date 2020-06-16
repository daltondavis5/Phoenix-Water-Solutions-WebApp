from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilityProviderViewSet, ProviderViewSet

router = DefaultRouter()
router.register('utilityprovider', UtilityProviderViewSet)
router.register('provider', ProviderViewSet)

urlpatterns = router.urls
