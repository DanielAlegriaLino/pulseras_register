from django.shortcuts import render, redirect
from .forms import t_registroForm
from .models import t_registro


def home(request):
    return render(request, 'home.html')
    
def registers(request):
    nombre = request.GET.get("cNombreCompleto", None)
    if(nombre):
        print(nombre)
        registros = t_registro.objects.filter(cNombreCompleto__contains=nombre)
        return render(request, 'registers.html', {'registros': registros})
    registros = t_registro.objects.all()
    return render(request, 'registers.html', {'registros': registros})

def FormRegistro(request):
    if request.method == 'POST':
        form = t_registroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registers')
    else:
        form = t_registroForm()
    return render(request, 'form.html', {'form': form})
