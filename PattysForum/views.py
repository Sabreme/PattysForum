from django.shortcuts import render, redirect

from post.models import Post
from .forms import SignupForm


def index(request):
    posts = Post.objects.filter()

    return render(request, 'index.html', {
        'posts': posts
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {
        'form': form
    })
