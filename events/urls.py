from django.urls import path
from . import views
from .views import delete_event, delete_comment

urlpatterns = [
    path('events/', views.event_view, name='event_view'),
    path('events/<int:event_post_id>/comment/', views.add_comment, name='add_comment'),
    path('like/<int:event_post_id>/', views.like_post, name='like_post'),
    path('edit-event/<int:event_post_id>/', views.edit_event, name='edit_event'),
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete-event/<int:post_id>/', delete_event, name='delete_event'),
    path('delete-comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]