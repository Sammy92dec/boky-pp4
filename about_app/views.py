from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm


def about(request):
    return render(request, 'about_app/about.html')

class PublishedPosts(generic.ListView):
    """
    View for listing published posts.
    """
    model = Post
    template_name = 'about_app/about.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        """
        Add context for pagination and title.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Published Posts'
        context['is_post_list'] = True 
        return context


class PostExpand(View):
    """
    View for displaying a single post and handling comments.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Render a single post with approved comments.
        """
        post = get_object_or_404(Post, status=1, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_date')

        return render(
            request, 'about_app/about.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm(),
                'is_post_detail': True,  # To distinguish in the template
            }
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handle comment submission.
        """
        post = get_object_or_404(Post, status=1, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_date')
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            try:
                comment.save()
                messages.success(request, 'Your comment is submitted and pending approval.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            messages.error(request, 'Invalid form. Please check your input.')

        return render(
            request, 'about_app/about.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                'is_post_detail': True,
            }
        )