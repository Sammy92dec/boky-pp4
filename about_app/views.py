from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.

def about(request):
    return HttpResponse("About is working test")

class PostList(generic.ListView):
    template_name = "about_app/index.html"
    paginate_by = 6