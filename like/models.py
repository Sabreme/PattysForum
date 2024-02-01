from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ('likes',)
        verbose_name_plural = 'Likes'

    def __str__(self):
        return self.user.username
