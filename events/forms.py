from django import forms
from .models import EventPost, EventComment

class EventPostForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = ['image', 'caption']  # Include only the fields users can set
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption'}),
        }

class EventCommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ['content']  # Users only need to input comment content
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...'}),
        }

def event_post_list(request):
    event_posts = EventPost.objects.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            event_post = form.save(commit=False)
            event_post.author = request.user
            event_post.save()
            return redirect('event_post_list')  # Redirect to the same page after posting
    else:
        form = EventPostForm()

    return render(request, 'event.html', {'event_posts': event_posts, 'form': form})