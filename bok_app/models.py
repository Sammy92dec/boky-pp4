from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Reasturant
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name
        

#Customer

class User(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

#Table 
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="tables")
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()  # Number of people the table can accommodate
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - {self.capacity} people"

#booking
class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="bookings")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")  # For how long the table is booked
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.customer.name} on {self.booking_date} at {self.booking_time}"

    class Meta:
        unique_together = ("table", "booking_date", "booking_time")   

#Check Status
STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled'),
]

status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')     