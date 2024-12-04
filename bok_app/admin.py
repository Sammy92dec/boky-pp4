from django.contrib import admin
from .models import Restaurant, Table, Client, Booking

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Client)
admin.site.register(Booking)