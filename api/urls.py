from django.urls import include, path, re_path

from api import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    re_path(r"^posts/search/(!:word=?P<word>\w+)?$", views.PostSearchView.as_view(), name='post-search'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('likes/', views.LikeListView.as_view(), name='like-list'),
    path('like/create', views.LikeCreateView.as_view(), name='like-create'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comment/create', views.CommentCreateView.as_view(), name='comment-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

