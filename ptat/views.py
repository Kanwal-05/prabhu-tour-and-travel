from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookingEnquiry

def index(request):
    return render(request, "Homepage.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method == "POST":
        BookingEnquiry.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            pickup_location=request.POST.get('pickup_location'),
            drop_location=request.POST.get('drop_location'),
            car_type=request.POST.get('car_type'),
            message=request.POST.get('message'),
        )
        return redirect('contact')  # reload page after submit

    return render(request, 'contact.html')

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin_once(request):
    if User.objects.filter(username="admin").exists():
        return HttpResponse("Admin already exists")

    User.objects.create_superuser(
        username="kanwal",
        email="gurkanwalsingh04@gmail.com",
        password="kanwal@5702"
    )
    return HttpResponse("Admin created successfully")




