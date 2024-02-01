from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    message = models.CharField(max_length=255)
    flagged = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ('likes',)
        verbose_name_plural = 'Posts'
        permissions = (
            ("regular_users", "Can Post, comment and Like"),
            ("moderator_users", "Can tag posts as misleading"),
        )

    def __str__(self):
        return self.message
