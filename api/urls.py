from django.urls import include, path, re_path

from api import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/search/v1/<str:word>/', views.PostSearchV1View.as_view(), name='post-search-v1'),
    # path('posts/search/v2/?word=<str:word>', views.PostSearchView.as_view(), name='post-search-v2'),
    # path('posts/search/v2/?word=message', views.PostSearchView.as_view(), name='post-search-v2'),
    re_path(r"^posts/search/v2/(!:word=?P<word>\w+)?$", views.PostSearchV2View.as_view(), name='post-search-v2'),
    # re_path(r"^posts/search/v2/(?P<word>\w+)/", views.PostSearchView.as_view(), name='post-search-v2'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('likes/', views.LikeListView.as_view(), name='like-list'),
    path('like/create', views.LikeCreateView.as_view(), name='like-create'),
    path('comments/', views.CommentListView.as_view(), name='comment-list'),
    path('comment/create', views.CommentCreateView.as_view(), name='comment-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

