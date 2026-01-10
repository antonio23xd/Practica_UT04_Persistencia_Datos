import uuid
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    TIPO_USUARIO = [
        ('ALUMNO', 'Alumno'),
        ('PROFESOR', 'Profesor'),
    ]
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=TIPO_USUARIO, default='ALUMNO')

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.fecha_nacimiento} {self.dni} {self.email} {self.rol}"

class Alumno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return f"Alumno: {self.usuario.nombre} {self.usuario.apellidos} {self.usuario.fecha_nacimiento} {self.usuario.dni} {self.usuario.email} {self.usuario.rol}"

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return f"Profesor: {self.usuario.nombre} {self.usuario.apellidos} {self.usuario.fecha_nacimiento} {self.usuario.dni} {self.usuario.email} {self.usuario.rol}"

#Modelo Tarea
class Tarea(models.Model):
    #Una de estos tipos de tarea puede ser evaluable o no
    #Eso se controla con un campo booleano
    TIPOS_TAREA = [
        ('INDIVIDUAL', 'Individual'),
        ('GRUPAL', 'Grupal'),
    ]    
    nombre_tarea = models.CharField(max_length=200)
    tipo_tarea = models.CharField(max_length=20, choices=TIPOS_TAREA)
    es_evaluable = models.BooleanField(default=False, blank=True, null=True)
    alumno_creador = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_entrega = models.DateTimeField()
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre_tarea} - {self.tipo_tarea} - {self.es_evaluable} - {self.fecha_creacion} - {self.fecha_entrega}"

class Tarea_Individual(Tarea):
    id_tarea_individual = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_tarea = models.CharField(max_length=20, choices=Tarea.TIPOS_TAREA, default='INDIVIDUAL')
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    profesores = models.ManyToManyField(Usuario, related_name='tarea_individual_profesores', blank=True)

    def __str__(self):
        return super().__str__() + f" - {self.alumno}"

class Tarea_Grupal(Tarea):
    id_tarea_grupal = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo_tarea = models.CharField(max_length=20, choices=Tarea.TIPOS_TAREA, default='GRUPAL')
    alumnos = models.ManyToManyField(Alumno, related_name='tareas_grupales_alumnos', blank=True)
    profesores = models.ManyToManyField(Profesor, related_name='tareas_grupales_profesores', blank=True)
    def __str__(self):
        return super().__str__() + f" - {self.alumno}"