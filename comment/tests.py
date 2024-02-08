from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Post
from .models import Comment


class CommentTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='test_user1', password='Abc123')
        self.user_2 = User.objects.create_user(username='test_user2', password='Abc123')

        login = self.client.login(username='test_user1', password='Abc123')
        self.test_post = Post.objects.create(message="Test Message 1", created_by=self.user_1)

    def test_comment_with_different_user_1_pass(self):
        """ Test the New Comment object created with new user"""
        client = Client()
        client.login(username='test_user2', password='Abc123')
        response = client.get("/posts/comment/1/", {"comment": "Test User Comment", "post": self.test_post, "user": self.user_2})
        self.assertEqual(Comment.objects.all().count(), 1)
