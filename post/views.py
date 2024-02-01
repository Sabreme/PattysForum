from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewPostForm
from .models import Post
from like.models import Like


@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect('post:detail', pk=post.id)

    else:
        form = NewPostForm()

    return render(request, 'form.html', {
        'form': form,
        'title': 'New Posting',
    })


def posts(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter().annotate(count_likes=Count('post_likes'))

    if query:
        posts = posts.filter(Q(message__icontains=query))

        for post in posts:
            print(post.message.count(query))
            post.frequency_count = post.message.count(query)

        reversed_post_list = sorted(posts, key=lambda s: s.frequency_count, reverse=True)

        return render(request, 'posts.html', {
            'posts': reversed_post_list,
            'query': query
        })

    else:
        return render(request, 'posts.html', {
            'posts': posts,
            'query': query
        })


@login_required
def detail(request, pk):
    post = Post.objects.filter(Q(pk=pk)).annotate(count_likes=Count('post_likes')).first()
    likes = Like.objects.filter(Q(post=post))

    return render(request, 'detail.html', {
        'post': post,
        'likes': likes,
    })


@login_required
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)

    not_already_liked = not Like.objects.filter(Q(user=request.user) & Q(post=post))
    not_own_post = request.user != post.created_by

    if not_own_post and not_already_liked:

        like = Like.objects.create(post=post, user=request.user)
        like.save()

    return redirect('post:detail', pk=pk)


@login_required
def flag(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not post.flagged:
        post.flagged = True
        post.save()

    return redirect('post:detail', pk=pk)
