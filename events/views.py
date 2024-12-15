from django.shortcuts import render, redirect, get_object_or_404
from .models import EventPost, EventComment, Like
from .forms import EventPostForm, EventCommentForm
from django.contrib.auth.decorators import login_required





def event_view(request):
    if request.method == 'POST':
        # Handle EventPost form submission
        if 'post_form' in request.POST:
            post_form = EventPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_form.instance.author = request.user
                post_form.save()
                return redirect('event_view')

        # Handle EventComment form submission
        elif 'comment_form' in request.POST:
            comment_form = EventCommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.instance.author = request.user
                comment_form.instance.event_post_id = request.POST.get('event_post_id')  # Associate comment with post
                comment_form.save()
                return redirect('event_view')
    else:
        post_form = EventPostForm()
        comment_form = EventCommentForm()
        

    # Prefetch related comments to optimize query
    event_posts = EventPost.objects.prefetch_related('event_comments').order_by('-created_at')

    return render(request, 'event_post/event.html', {
        'post_form': post_form,
        'comment_form': comment_form,
        'event_posts': event_posts,
    })

def edit_event(request, event_post_id):
    event_post = get_object_or_404(EventPost, id=event_post_id)
    if request.user != event_post.author:
        # You could redirect to the event page or display a message
        return redirect('event_view')  # or show an error message
    
    if request.method == 'POST':
        form = EventPostForm(request.POST, request.FILES, instance=event_post)
        if form.is_valid():
            form.save()
            return redirect('event_view')
    else:
        form = EventPostForm(instance=event_post)
    
    return render(request, 'event_post/edit_event.html', {'form': form})


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
    return redirect('event_view')  # or wherever you want to redirect after liking