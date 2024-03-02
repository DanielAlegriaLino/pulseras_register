from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import t_registroForm
from .models import t_registro
import psycopg2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def home(request):
    return render(request, 'home.html')
    
def registers(request):
    verificador = 0
    nombre = request.GET.get("cNombreCompleto", None)
    if nombre:
        registros = t_registro.objects.filter(Q(cNombreCompleto__contains=nombre) | Q(cPaisEmpresa__contains=nombre) | Q(cModalidadActividad__contains=nombre))
    else:
        registros = t_registro.objects.all().order_by('-dFecha')

    paginator = Paginator(registros, 35)  # 10 registros por página
    page = request.GET.get('page')

    try:
        registros_pagina = paginator.page(page)
    except PageNotAnInteger:
        registros_pagina = paginator.page(1)
    except EmptyPage:
        registros_pagina = paginator.page(paginator.num_pages) 

    if request.method == 'POST':
        id_reg = request.POST.get('id_r')
        n_braz = request.POST.get('n_bz')
        registro_asignar = get_object_or_404(t_registro, nIdRegistro=id_reg)
        registro_asignar.cBrazalete = n_braz
        registro_asignar.save()
    return render(request, 'registers.html', {'registros': registros_pagina,'verificador': verificador})

def registers_or(request):
    input_value = request.GET.get('selected_buttons', '')
    valores = input_value.split(',')
    
    nombre = request.GET.get("cNombreCompleto", None)
    if nombre:
        registros = t_registro.objects.filter(Q(cNombreCompleto__contains=nombre) | Q(cPaisEmpresa__contains=nombre))
    else:
        registros = t_registro.objects.all().order_by(*valores)
            

    paginator = Paginator(registros, 35)  # 10 registros por página
    page = request.GET.get('page')

    try:
        registros_pagina = paginator.page(page)
    except PageNotAnInteger:
        registros_pagina = paginator.page(1)
    except EmptyPage:
        registros_pagina = paginator.page(paginator.num_pages) 

    if request.method == 'POST':
        id_reg = request.POST.get('id_r')
        n_braz = request.POST.get('n_bz')
        registro_asignar = get_object_or_404(t_registro, nIdRegistro=id_reg)
        registro_asignar.cBrazalete = n_braz
        registro_asignar.save()

    return render(request, 'registers-copy.html', {'registros': registros_pagina, 'valores': valores})

def FormRegistro(request):
    if request.method == 'POST':
        form = t_registroForm(request.POST)
        if form.is_valid():
            NuevoRegistro = form.save(commit=False)
            NuevoRegistro.nIdRegistro = Exclusiveid()
            NuevoRegistro.save()
            return redirect('forms-register')
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
            percentage = round((count / entire) * 100,2)
            counts.append(count)
            percentages.append(percentage)
           
        cursor.execute('SELECT COUNT(*) FROM "t_registro" WHERE "cBrazalete" = 0')
        cursor.close()
        conn.commit()
    except psycopg2.Error as e:
        return HttpResponse("La base de datos no responde, contacte a los desarrolladores")
    finally:
        conn.close()
    
    colores=["No asignado","Amarillo", "Naranja", "Verde", "Azul", "Rosa", "Morado"]
    nombres = ["No asignado", "Staff", "Expositor", "Colaborador", "VIP", "Artista", "Comunicación"]
    return render(request, 'corte.html', {
        'total_count': entire,
        'counts_percentages_colors':zip(counts,percentages, colores, nombres),
    })
    return HttpResponse("Summary")

def Exclusiveid():
    last_id = t_registro.objects.latest('nIdRegistro').nIdRegistro
    return last_id + 1
    
    
    