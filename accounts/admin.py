from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address')  # Columns in admin list view
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')  # Enable search
    list_filter = ('email',)  # Add filtering options

admin.site.register(Client, ClientAdmin)
