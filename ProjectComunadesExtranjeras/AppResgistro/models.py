from django.db import models

class t_registro(models.Model):
    nIdRegistro = models.AutoField(primary_key=True)  
    cNombreCompleto = models.TextField()  
    cPaisEmpresa = models.TextField() 
    cModalidadActividad = models.TextField()  
    dFecha = models.DateField(auto_now_add=True)  
    tHora = models.TimeField(auto_now_add=True)  
    cBrazalete  = models.TextField()

    class Meta:
        managed = False
        db_table = 't_registro'

