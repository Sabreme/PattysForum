from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('new/', views.new_post, name='new'),
    path('<int:pk>/', views.detail, name='detail')
]
