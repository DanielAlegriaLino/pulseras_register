from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import t_registroForm
from .models import t_registro
import psycopg2

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

def getSummary(request):
    total_count = 0
    percentages = []
    counts = []
    entire = 0
    host = 'server-comunidadesextranjeras.postgres.database.azure.com'
    dbname = 'bdcomext'
    user = 'Erick'
    password = 'xiCxyp-qezgi9-tuwkam'
    
    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM t_registro")
        
                # Obtener resultado
        entire = cursor.fetchone()[0]
        value_look = [0,1, 2, 3, 4, 5, 6, 7]
        
        for value in value_look:
            cursor.execute(f'SELECT COUNT(*) FROM "t_registro" WHERE "cBrazalete" = {value}')
            count = cursor.fetchone()[0]
            percentage = (count / entire) * 100
            counts.append(count)
            percentages.append(percentage)
           
        cursor.execute('SELECT COUNT(*) FROM "t_registro" WHERE "cBrazalete" = 0')
        cursor.close()
        conn.commit()
    except psycopg2.Error as e:
        return HttpResponse("La base de datos no responde, contacte a los desarrolladores")
    finally:
        conn.close()
        
    print(counts)
    print(percentages)
    print(entire)
    
    colores=["No asignado","Amarillo", "Naranja", "Verde", "Azul", "Rosa", "Morado"]
    return render(request, 'corte.html', {
        'total_count': entire,
        'counts_percentages_colors':zip(counts,percentages, colores),
    })
    return HttpResponse("Summary")
    
    
    