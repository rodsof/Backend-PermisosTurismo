from django.db import models
from django.db.models.fields import CharField
import datetime

# Modelo de Evento
class Evento(models.Model):
    idEvento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

# Modelo de Domicilio
class Domicilio(models.Model): 
    idDomicilio = models.AutoField(primary_key=True)
    idProvincia = models.CharField(max_length=45)
    idDepartamento = models.CharField(max_length=45)
    idLocalidad = models.CharField(max_length=45)
    calle = models.CharField(max_length=45, null=True, blank=True)
    nro = models.CharField(max_length=45, null=True, blank=True)
    piso = models.CharField(max_length=45, null=True, blank=True)
    depto = models.CharField(max_length=45, null=True, blank=True)
    latLocalidad = models.CharField(max_length=45)
    longLocalidad = models.CharField(max_length=45)

# Modelo de Ciudadanos
class Ciudadano(models.Model):
    idCiudadano = models.AutoField(primary_key=True)
    cuil = models.CharField(unique=True,max_length=45) # Agrega ciudadano siempre y cuando no exista ya un registro con el cuil agregar.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    nroDoc = models.CharField(unique=True,max_length=45)
    nroTramite = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=45, null=True, blank=True)
    extranjero = models.CharField(max_length=45, null=True)
    sexo = models.CharField(max_length=45, null=True)

# Modelo de Permiso
class Permiso(models.Model):
    codigoPermiso = models.AutoField(primary_key=True) # codPermiso consecutivo, autoincremental de 6 cifras, esto último está especificado en la bd
    fechaGeneracion = models.DateField(default=datetime.date.today) # La fecha actual de generación del permiso
    fecha = models.DateField() # Fecha de ingreso 
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)


