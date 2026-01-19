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




