from django.contrib import admin
from .models import Restaurant, Table, Customer, Booking

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Customer)
admin.site.register(Booking)