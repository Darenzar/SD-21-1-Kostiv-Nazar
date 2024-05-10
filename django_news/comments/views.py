from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm
from .models import Comment


def create_comment_view(request, pk):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        form.instance.post_id = pk
        form.instance.author = request.user
        form.save()
        return redirect('index')
    return render(request, 'comments/create_comment.html', {'form': form})


def delete_comment_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('index')
    return render(request, 'comments/delete_comment.html', {'comment': comment})
