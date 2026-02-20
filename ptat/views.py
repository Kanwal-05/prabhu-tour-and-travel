# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import BookingEnquiry

# from django.http import HttpResponse
# from django.db import connection
# def index(request):
#     return render(request, "Homepage.html")
# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return render(request, "contact.html")
# def services(request):
#     return render(request, "services.html")


# def contact(request):
#     if request.method == "POST":
#         BookingEnquiry.objects.create(
#             name=request.POST.get("name"),
#             phone=request.POST.get("phone"),
#             pickup_location=request.POST.get("pickup_location"),
#             drop_location=request.POST.get("drop_location"),
#             car_type=request.POST.get("car_type"),
#             message=request.POST.get("message"),
#         )
#         return redirect("contact")

#     return render(request, "contact.html")




# def run_migrations_once(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT 1")
#     return HttpResponse("Database connected")


from django.shortcuts import render
from django.http import HttpResponse
import requests


# 🔹 Paste your Apps Script URL here
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbyxeCBX3y7da8Wdo8clI7Yz2OtDGJiQUcmH0gkcl0GuVVraFvZiFiKMFq8QZHZZ4Itg9Q/exec"


def index(request):
    return render(request, "Homepage.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "phone": request.POST.get("phone"),
            "pickup_location": request.POST.get("pickup_location"),
            "drop_location": request.POST.get("drop_location"),
            "car_type": request.POST.get("car_type"),
            "message": request.POST.get("message"),
        }

        try:
            requests.post(WEBHOOK_URL, json=data)
        except:
            pass  # prevents crash if something fails

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")



