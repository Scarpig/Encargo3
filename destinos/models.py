from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class cotizacion(models.Model):
    
    nombre=models.CharField(max_length=200, help_text='ingrese su lugar de destino')
    rut=models.CharField(max_length=12, help_text='ingrese su rut con puntos y guion', primary_key=True)
    email=models.EmailField()
    mensaje=models.CharField(max_length=200, help_text='escriba su mensaje')


    class Meta:
        ordering =['nombre']


    def get_absolute_url(self):
        return reverse('cotizacion-detail',args=[str(self.rut)])

    def str(self):
        return f'{self.nombre},{self.rut},{self.email},{self.mensaje}'
