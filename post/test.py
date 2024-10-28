from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like, Follow
from django.db import IntegrityError


class SocialMediaTestCase(TestCase):

    def setUp(self):
        # Cria usuários
        self.user1 = User.objects.create_user(username="user1", password="password1")
        self.user2 = User.objects.create_user(username="user2", password="password2")

        # Cria postagens
        self.post1 = Post.objects.create(
            user=self.user1, content="First Post by User 1"
        )
        self.post2 = Post.objects.create(
            user=self.user2, content="First Post by User 2"
        )

    # Testes para o Modelo Post
    def test_create_post(self):
        post = Post.objects.create(user=self.user1, content="New Post by User 1")
        self.assertEqual(post.user, self.user1)
        self.assertEqual(post.content, "New Post by User 1")

    def test_edit_post(self):
        self.post1.content = "Edited Content"
        self.post1.save()
        self.assertEqual(self.post1.content, "Edited Content")

    def test_delete_post(self):
        post_id = self.post1.id
        self.post1.delete()
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=post_id)

    # Testes para o Modelo Like
    def test_like_post(self):
        like = Like.objects.create(user=self.user1, post=self.post2)
        self.assertEqual(like.user, self.user1)
        self.assertEqual(like.post, self.post2)

    def test_unique_like(self):
        # Um usuário só pode curtir uma postagem uma vez
        Like.objects.create(user=self.user1, post=self.post2)
        with self.assertRaises(IntegrityError):
            Like.objects.create(user=self.user1, post=self.post2)

    def test_unlike_post(self):
        like = Like.objects.create(user=self.user1, post=self.post2)
        like_id = like.id
        like.delete()
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like_id)

    # Testes para o Modelo Follow
    def test_follow_user(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.following, self.user2)

    def test_unique_follow(self):
        # Um usuário só pode seguir outro uma vez
        Follow.objects.create(follower=self.user1, following=self.user2)
        with self.assertRaises(IntegrityError):
            Follow.objects.create(follower=self.user1, following=self.user2)

    def test_unfollow_user(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        follow_id = follow.id
        follow.delete()
        with self.assertRaises(Follow.DoesNotExist):
            Follow.objects.get(id=follow_id)

    # Teste do Feed
    def test_feed(self):
        # Usuário 1 segue Usuário 2
        Follow.objects.create(follower=self.user1, following=self.user2)

        # Usuário 1 deve ver as postagens de Usuário 2
        feed_posts = Post.objects.filter(
            user__in=self.user1.following.values("following")
        )
        self.assertIn(self.post2, feed_posts)

        # Usuário 1 não deve ver suas próprias postagens no feed de seguidos
        self.assertNotIn(self.post1, feed_posts)

    # Testes adicionais
    def test_cascade_delete_post_likes(self):
        # Curtir uma postagem e deletar a postagem
        like = Like.objects.create(user=self.user1, post=self.post2)
        post_id = self.post2.id
        self.post2.delete()

        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like.id)

        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=post_id)

    def test_cascade_delete_user_posts_and_follows(self):
        # Criar postagens e follows, e deletar o usuário
        Follow.objects.create(follower=self.user1, following=self.user2)
        post = Post.objects.create(user=self.user1, content="Post to be deleted")

        self.user1.delete()

        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=post.id)

        with self.assertRaises(Follow.DoesNotExist):
            Follow.objects.get(follower=self.user1, following=self.user2)
