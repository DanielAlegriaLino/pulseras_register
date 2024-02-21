from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from AppResgistro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registros/', views.registers, name="registers"),
]

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)