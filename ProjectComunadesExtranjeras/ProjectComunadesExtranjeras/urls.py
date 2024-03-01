from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from AppResgistro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registros/', views.registers, name="registers"),
    path('registros/<str:search>', views.registers, name="registers"),
    path('NuevoRegistro/', views.FormRegistro, name="forms-register"),
    path('corte/', views.getSummary, name="getSummary"),
    path('ordenar_registros/', views.ordenar_registros, name='ordenar_registros'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)