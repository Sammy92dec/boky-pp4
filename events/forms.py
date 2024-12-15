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
