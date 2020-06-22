from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ListUtilities, UtilityProviderViewSet

router = DefaultRouter()
router.register('provider', ProviderViewSet)
router.register('utility_provider', UtilityProviderViewSet)

urlpatterns = [
    path('utility/', ListUtilities.as_view(), name='utility-list'),
]

urlpatterns += router.urls
