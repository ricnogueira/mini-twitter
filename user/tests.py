from django.test import TestCase
# tests.py
from django.contrib.auth.models import User
from django.urls import reverse
from follow.models import Follow
from like.models import Like
from post.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegisterTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("user-register")  # URL para o registro

    def test_user_registration(self):
        """
        Teste se um novo usuário pode ser registrado com sucesso.
        """
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "securepassword123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_user_registration_with_existing_username(self):
        """
        Teste que um erro é retornado ao tentar registrar um usuário com um nome de usuário já existente.
        """
        User.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="password123",
        )
        data = {
            "username": "existinguser",
            "email": "newuser@example.com",
            "password": "securepassword123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_registration_with_missing_fields(self):
        """
        Teste que um erro é retornado ao tentar registrar um usuário sem campos obrigatórios.
        """
        data = {
            "username": "",
            "email": "missing@example.com",
            "password": "securepassword123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_registration_with_invalid_email(self):
        """
        Teste que um erro é retornado ao tentar registrar um usuário com um email inválido.
        """
        data = {
            "username": "testuser2",
            "email": "not-an-email",
            "password": "securepassword123",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
