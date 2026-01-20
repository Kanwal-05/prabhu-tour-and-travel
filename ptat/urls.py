from django.contrib import admin
from django.urls import path
from ptat import views


admin.site.site_header = "Prabhu Tour & Travels Admin"
admin.site.site_title = "Prabhu Tour & Travels"
admin.site.index_title = "Welcome to Prabhu Tour & Travels Portal"
urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.services, name="services"),
    path("db-check/", views.run_migrations_once),

]

