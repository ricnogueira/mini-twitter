from django.test import TestCase
from django.contrib.auth.models import User
from follow.models import Follow
from django.core.exceptions import ValidationError


class FollowTestCase(TestCase):

    def setUp(self):
        # Criação de usuários
        self.user1 = User.objects.create_user(username="user1", password="password1")

    def test_user_cannot_follow_self(self):
        # Tentativa de seguir a si mesmo deve gerar um erro de validação
        follow = Follow(follower=self.user1, following=self.user1)
        with self.assertRaises(ValidationError):
            follow.save()
