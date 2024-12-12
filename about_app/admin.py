from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post



@admin.register(Post)


class PostAdmin(SummernoteModelAdmin):

    
    list_display = ('title', 'slug', 'status', 'published_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ()





