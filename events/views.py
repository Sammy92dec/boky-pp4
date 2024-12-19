from django.shortcuts import render, redirect, get_object_or_404
from .models import EventPost, EventComment, Like
from .forms import EventPostForm, EventCommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def event_view(request):
    post_form = None
    comment_form = None
    event_posts = EventPost.objects.all()

    if request.method == 'POST' and request.user.is_authenticated:
        if 'post_form' in request.POST:
            post_form = EventPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                event_post = post_form.save(commit=False)
                event_post.author = request.user
                event_post.save()
                return redirect('event_post_list')
        elif 'comment_form' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                post = EventPost.objects.get(id=request.POST.get('post_id'))
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('event_view')
    else:
        post_form = EventPostForm()
    
    return render(request, 'event_post/event.html', {
        'event_posts': event_posts,
        'post_form': post_form,
        'comment_form': comment_form
    })
    

@login_required
def edit_event(request, post_id):
    post = get_object_or_404(EventPost, id=post_id, author=request.user)
    if request.method == 'POST':
        form = EventPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('event_view')  # or wherever you want to go after editing
    else:
        form = EventPostForm(instance=post)

    return render(request, 'event_post/edit_event.html', {'form': form, 'post': post})
@login_required
def add_comment(request, event_post_id):
    event_post = get_object_or_404(EventPost, id=event_post_id)
    if request.method == 'POST':
        comment_form = EventCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.event_post = event_post
            comment.save()
            return redirect('event_view')  # Redirect back to event listing page after comment
    else:
        comment_form = EventCommentForm()

    return render(request, 'event.html', {'comment_form': comment_form, 'event_post': event_post})

@login_required
def edit_comment(request, comment_id):
    # Get the comment to edit
    comment = get_object_or_404(EventComment, id=comment_id)

    # Ensure that the current user is the author of the comment
    if comment.author != request.user:
        return redirect('event_view')  # Redirect to the event page if the user is not the author

    # Handle the form submission
    if request.method == 'POST':
        comment_form = EventCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()  # Save the updated comment
            return redirect('event_view')
    else:
        comment_form = EventCommentForm(instance=comment)  # Populate the form with the existing comment data

    # Render the edit page
    return render(request, 'event_post/edit_comment.html', {
        'comment_form': comment_form,
        'comment': comment
    })

@login_required
def like_post(request, event_post_id):
    event_post = EventPost.objects.get(id=event_post_id)
    # Check if the user has already liked the post
    if not Like.objects.filter(user=request.user, event_post=event_post).exists():
        Like.objects.create(user=request.user, event_post=event_post)
    else:
        Like.objects.filter(user=request.user, event_post=event_post).delete()
    return redirect('event_view')   # or wherever you want to redirect after liking


@login_required
def delete_event(request, post_id):
    post = get_object_or_404(EventPost, id=post_id)
    # Ensure only the author can delete the post
    if post.author == request.user:
        post.delete()
        return redirect('event_view')  # Redirect back to event listing or wherever appropriate
    else:
        # If the user is not the author, you might want to show an error or just redirect
        return redirect('event_view')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(EventComment, id=comment_id)
    # Ensure only the author can delete the comment
    if comment.author == request.user:
        comment.delete()
        return redirect('event_view')  # Redirect to a page showing the event posts
    else:
        return redirect('event_view')  # or return an error message

@login_required
def create_event_post(request):
    if request.method == "POST":
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            event_post = form.save(commit=False)
            event_post.author = request.user
            event_post.save()
            return redirect('event_view')  # Redirect to the post list view
    else:
        form = EventPostForm()
    return redirect('event_view')