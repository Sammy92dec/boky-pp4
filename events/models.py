from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class EventPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_posts')
    image = CloudinaryField('image')
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.author.username}'s post"

class EventComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event_post = models.ForeignKey(EventPost, related_name='event_comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on EventPost {self.event_post.id}"

class Like(models.Model):
    event_post = models.ForeignKey(EventPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event_post', 'user')  # Ensures a user can like a post only once

    def __str__(self):
        return f"{self.user.username} liked EventPost {self.event_post.id}"