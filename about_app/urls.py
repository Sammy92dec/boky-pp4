from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='home'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('', views.post_list, name='post_list'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/', views.comment_list, name='comment_list'),
]