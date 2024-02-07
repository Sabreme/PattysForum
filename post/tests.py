from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='Abc123')
        login = self.client.login(username='test_user', password='Abc123')
        Post.objects.create(message="Test Message 1", created_by=self.user)

    def test_post_flagged(self):
        """Test that a post flag is applied"""

        test_post = Post.objects.get(message="Test Message 1")
        test_post.flagged = True
        self.assertEqual(test_post.flagged, True)

    def test_details_page_no_login_error(self):
        """ Test the Post Detail Page no login Failure"""
        client = Client()
        response = client.get("/posts/1/")
        self.assertNotEqual(response.status_code, 200)

    def test_details_page_with_login_pass(self):
        """ Test the Post Detail Page with login Pass"""
        client = Client()
        client.login(username='test_user', password='Abc123')
        response = client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)
