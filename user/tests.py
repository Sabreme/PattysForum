from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, Client

from post.models import Post


class UserPermissionTestCase(TestCase):
    def setUp(self):

        content_type = ContentType.objects.get_for_model(Post)
        post_permissions = Permission.objects.filter(content_type=content_type)

        self.user_1 = User.objects.create_user(username='test_user1', password='Abc123')

        self.user_2 = User.objects.create_user(username='test_user2', password='Abc123')

        moderator_permission = post_permissions.get(codename="moderator_users")
        self.user_2.user_permissions.add(moderator_permission)

    def test_user_1_permissions_fail(self):
        """ Test the user 1 with NO permissions to moderate ie: Flag misleading"""
        client = Client()
        client.login(username='test_user1', password='Abc123')
        self.assertEqual(self.user_1.has_perm("post.moderator_users"), False)

    def test_user_2_permissions_pass(self):
        """ Test the New Like object created with new user"""
        client = Client()
        client.login(username='test_user2', password='Abc123')
        self.assertEqual(self.user_2.has_perm("post.moderator_users"), True)
