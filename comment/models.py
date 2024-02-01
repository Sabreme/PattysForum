from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ('likes',)
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.user.username
