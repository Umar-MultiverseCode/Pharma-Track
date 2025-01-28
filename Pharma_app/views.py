from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
 

# Create your views here.
def home(request):
    return render(request,'landing.html')

