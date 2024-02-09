from django.http import JsonResponse
from django.utils.timezone import make_aware

from post.models import Post
from like.models import Like
from comment.models import Comment

from datetime import datetime, timedelta


def metrics(request):

    native_datetime = make_aware(datetime.today())
    last_day = native_datetime - timedelta(days=1)

    posts = Post.objects.filter().all()
    likes = Like.objects.filter().all()
    comments = Comment.objects.filter().all()

    hours_posts = {}
    hours_likes = {}
    hours_comments = {}

    day_posts = 0
    day_likes = 0
    day_comments = 0

    for hour in range(0, 24):
        hour_start = last_day + timedelta(hours=hour)
        hour_end = last_day + timedelta(hours=hour + 1)

        hours_posts[hour] = posts.filter(created_at__gte=hour_start, created_at__lt=hour_end).count()
        day_posts += hours_posts[hour]

        hours_likes[hour] = likes.filter(created_at__gte=hour_start, created_at__lt=hour_end).count()
        day_likes += hours_likes[hour]

        hours_comments[hour] = comments.filter(created_at__gte=hour_start, created_at__lt=hour_end).count()
        day_comments += hours_comments[hour]

    print(hours_posts)
    print(hours_likes)
    print(hours_comments)

    response_data = {}

    response_data['Posts_in_last_day'] = day_posts
    response_data['Likes_in_last_day'] = day_likes
    response_data['Comments_in_last_day'] = day_comments

    response_data['hours_posts'] = hours_posts
    response_data['hours_likes'] = hours_likes
    response_data['hours_comments'] = hours_comments

    return JsonResponse(response_data)
