from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Post
from .models import Like


class LikeTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='test_user1', password='Abc123')
        self.user_2 = User.objects.create_user(username='test_user2', password='Abc123')

        login = self.client.login(username='test_user1', password='Abc123')
        self.test_post = Post.objects.create(message="Test Message 1", created_by=self.user_1)

    def test_like_with_same_user_1_fail(self):
        """ Test the New Like cannot work with same user"""
        client = Client()
        client.login(username='test_user1', password='Abc123')
        response = client.post("/posts/like/1/", {"post": self.test_post, "user": self.user_1})
        self.assertEqual(Like.objects.all().count(), 0)

    def test_like_with_different_user_1_pass(self):
        """ Test the New Like Succeed with new user"""
        client = Client()
        client.login(username='test_user2', password='Abc123')
        response = client.post("/posts/like/1/", {"post": self.test_post, "user": self.user_2})
        self.assertEqual(response.status_code, 200)

