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
    path('registers_or/<int:n>', views.registers_or, name='registers_or'),
    path('registers_or/<int:n>/<int:a>', views.registers_or, name='registers_or_with'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)