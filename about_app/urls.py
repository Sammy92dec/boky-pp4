from . import views
from django.urls import path


urlpatterns = [
    path('about/', views.PublishedPosts.as_view(), name='about_us'),
    path('post/<slug:slug>/', views.PostExpand.as_view(), name='post_expand'),
]

