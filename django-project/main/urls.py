from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ListUtilities

router = DefaultRouter()
router.register('provider', ProviderViewSet)

urlpatterns = [
    path('utility/', ListUtilities.as_view(), name='utility-list')
]

urlpatterns += router.urls
