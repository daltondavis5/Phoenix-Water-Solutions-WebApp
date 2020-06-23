from django.urls import path, include
from .views import UserAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('', include('knox.urls')),
    path('login', LoginAPI.as_view(), name='login'),
    path('user', UserAPI.as_view(), name='user'),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
