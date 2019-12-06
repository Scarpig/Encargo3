from django.test import TestCase
from destinos.models import cotizacion


class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cotizacion.objects.create(nombre = "elyeferson",rut="20052182k",email="mati_x@hotmail.com",mensaje="hot hot hot")
    def test_nombre_label(self):

        cot= cotizacion.objects.get(rut = '20052182k')
        field_label = cot._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')