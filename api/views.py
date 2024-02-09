from django.urls import resolve
from rest_framework import generics, permissions
from post.models import Post
from like.models import Like
from comment.models import Comment

from api.serializers import PostSerializer
from api.serializers import LikeSerializer
from api.serializers import CommentSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get']


class PostSearchView(generics.ListAPIView):
    """
    This is used when search word is used as query parameter such as in Postman
    """
    serializer_class = PostSerializer
    http_method_names = ['get']

    def get_queryset(self):
        search_word = self.request.GET.get('word')
        filtered_posts = Post.objects.filter(message__icontains=search_word)
        for post in filtered_posts:
            post.search_count = post.message.count(search_word)

        reversed_post_list = sorted(filtered_posts, key=lambda p: p.search_count, reverse=True)

        return reversed_post_list


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['get']


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get']