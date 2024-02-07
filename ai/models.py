from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class PredictedLikes(models.Model):
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, related_name='post_predicted_likes', on_delete=models.CASCADE)
    users = models.ManyToManyField(to=User, related_name="users_predicted")
    like_ratio = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'PredictedLikes'

    def __str__(self):
        return str(self.likes)
