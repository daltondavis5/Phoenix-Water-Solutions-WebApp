from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilityProviderViewSet

router = DefaultRouter()
router.register('utilityprovider', UtilityProviderViewSet)

urlpatterns = router.urls
