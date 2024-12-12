from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.food, name='foods'),
    path('drinks/', views.drink, name='drinks'),
]