from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.


class CategoriaEmpresa(models.Model):
   id = models.UUIDField(primary_key = True, default = uuid4)
   nombre = models.CharField(max_length = 30)


class PerfilEmpresa(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4)
  imagenes_empresa = models.ImageField( upload_to='perfil_empresa', blank=True )
  mision= models.CharField(max_length=1500)
  vision = models.CharField(max_length=600)
  servicios = models.CharField(max_length=500)
  categoria = models.ForeignKey(CategoriaEmpresa, on_delete = models.CASCADE)


class Empresa (models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4)
  nombre = models.CharField(max_length = 30)
  nombre_propietario = models.CharField(max_length = 30)
  direccion = models.CharField(max_length = 1000)
  url= models.URLField()
  telefono= models.CharField (max_length=50)
  perfil_empresa =models.ForeignKey(PerfilEmpresa, default = uuid4, on_delete= models.CASCADE)


class Valoracion(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid4)
  calificacion = models.FloatField(default = 0)
  fecha_valoracion = models.DateField( )
  comentarios = models.CharField(max_length=50000)
  empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)
