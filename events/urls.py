from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_view, name='event_view'),
    path('events/<int:event_post_id>/comment/', views.add_comment, name='add_comment'),
    path('like/<int:event_post_id>/', views.like_post, name='like_post'),
    path('edit-event/<int:event_post_id>/', views.edit_event, name='edit_event'),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
]