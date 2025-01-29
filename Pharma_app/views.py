from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages 

def landing_page(request):
    return render(request, 'landing.html')
def dashboard(request):
    return render(request, 'dashboard.html')

def inventory(request):
    return render(request, 'inventory.html')

def quality_control(request):
    return render(request, 'quality_control.html')

def distribution(request):
    return render(request, 'distribution.html')

def compliance(request):
    return render(request, 'compliance.html')

def analytics(request):
    return render(request, 'analytics.html')

def settings(request):
    return render(request, 'settings.html')