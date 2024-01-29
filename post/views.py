from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewPostForm
from .models import Post


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
    posts = Post.objects.filter()

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


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # related_items = Post.objects.filter()

    return render(request, 'detail.html', {
        'post': post,
    })
