from . import views
from django.urls import path


app_name = 'about_app'

urlpatterns = [
    path('about/', about_views.about, name='about'),
    path('', views.PublishedPosts.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostExpand.as_view(), name='post_detail'),
]