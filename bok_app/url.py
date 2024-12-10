from django.urls import path
from . import index_views  # Import the index_views


urlpatterns = [
    path('menu/', views.index, name='user'),  # Home page
]