from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    message = models.CharField(max_length=255)
    likes = models.IntegerField(blank=True, null=True)
    flagged = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ('likes',)
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.message
