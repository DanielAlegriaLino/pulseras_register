from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')
    
def registers(request):
    return render(request, 'registers.html')
