from django.urls import path
from . import index_views  # Import the index_views


urlpatterns = [
    path('', views.index, name='home'),  # Home page
]