from django.urls import reverse

from accounts.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.serializers import UserSerializer
from knox.models import AuthToken


class TestUserAPI(APITestCase):
    def setUp(self):
        User.objects.create_user(
            "testUser", "testemail@test.com", "testPass")

    def test_anonymous_cannot_get_user(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_get_user(self):
        user = User.objects.get(username="testUser")
        token = AuthToken.objects.create(user)[1]
        self.client.force_login(user=user)
        response = self.client.get(
            reverse('user'), HTTP_AUTHORIZATION='Token ' + token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request_can_login(self):
        data = {
            "username": "testUser",
            "password": "testPass"
        }

        response = self.client.post(reverse("login"), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
