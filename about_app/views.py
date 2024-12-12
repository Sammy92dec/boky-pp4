from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment


def about(request):
    return render(request, 'about_app/about.html')

def post_list(request):
    posts = Post.objects.all().filter(published_date__lte=timezone.now())
    return render(request, 'about_app/post_list.html', {'posts': posts})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'about_app/post_list.html', {'comments': comments})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "about_app/post_details.html",{'posts': posts})



