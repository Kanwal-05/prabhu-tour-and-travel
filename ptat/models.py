
from django.db import models

class BookingEnquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    pickup_location = models.CharField(max_length=200)
    drop_location = models.CharField(max_length=200)
    car_type = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
