from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post

from .forms import PostForm


def index_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def post_create_view(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=False)
        form.instance.created_by = request.user
        form.save()
        return redirect('index')
    return render(request, 'posts/create_form.html', {'form': form})


@login_required
def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'posts/update_form.html', {'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'posts/delete_form.html', {'post': post})
