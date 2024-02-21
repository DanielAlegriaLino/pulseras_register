from django.shortcuts import render, HttpResponse
from django.urls import get_resolver


def home(request):
    return render(request, 'home.html')
    
def registers(request):
    return render(request, 'registers.html')
