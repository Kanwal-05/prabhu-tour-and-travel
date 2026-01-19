from django.contrib import admin

from django.contrib import admin
from .models import BookingEnquiry

@admin.register(BookingEnquiry)
class BookingEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'pickup_location',
        'drop_location',
        'car_type',
        'created_at',
    )
    search_fields = ('name', 'phone', 'pickup_location', 'drop_location')
    list_filter = ('car_type', 'created_at')
