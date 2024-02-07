from django.db.models import Q, Count
from .models import Post
from ai.models import PredictedLikes

import math


def analytics(new_post):
    """
        The algorithm used here is the following - claiming it as an proportionate like ratio
        - Get all the posts that have had likes before as the baseline
        - examine the contents of the posts and see overlapping of words
        - determine the ratio of common words for that post and assign that ratio to the likes
        - repeat for all the posts
        - apply that ratio to the number of users who liked the above because users can only like a post once
    """
    predicted_likes = PredictedLikes.objects.create(post=new_post)

    total_like_ratio_list = []
    user_set = set()

    liked_posts = Post.objects.annotate(count_likes=Count('post_likes')).filter(count_likes__gt=0)

    content_new_post_set = set(map(str.lower, (new_post.message.split())))

    for old_post in liked_posts:
        content_old_post_set = set(map(str.lower, old_post.message.split()))
        likes_old_post = old_post.count_likes
        common_words_set = content_new_post_set.intersection(content_old_post_set)
        word_ratio = len(common_words_set) / len(content_old_post_set)
        total_like_ratio_list.append(word_ratio * likes_old_post)

        if word_ratio > 0:
            old_post_likes = old_post.post_likes.all().all()

            for old_post_like in old_post_likes:
                if old_post_like.user != new_post.created_by:
                    user_set.add(old_post_like.user)
                    predicted_likes.users.add(old_post_like.user)

    liked_users_count = len(user_set)
    total_like_ratio = sum(total_like_ratio_list) / len(total_like_ratio_list)
    future_likes = math.ceil(total_like_ratio * liked_users_count)

    predicted_likes.likes = future_likes
    predicted_likes.like_ratio = total_like_ratio

    predicted_likes.save()
