import uuid
from django.db import models

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
    TIPOS_TAREA = [
        ('INDIVIDUAL', 'Individual'),
        ('GRUPAL', 'Grupal'),
        ('EVALUABLE', 'Evaluable'),
    ]    
    nombre_tarea = models.CharField(max_length=200)
    tipo_tarea = models.CharField(max_length=20, choices=TIPOS_TAREA)
    es_evaluable = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField()
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre_tarea} - {self.tipo_tarea} - {self.es_evaluable} - {self.fecha_creacion} - {self.fecha_entrega}"

class Tarea_Individual(Tarea):
    id_tarea_individual = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)    

    def __str__(self):
        return super().__str__() + f" - {self.alumno}"

class Tarea_Grupal(Tarea):
    id_tarea_grupal = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + f" - {self.alumno}"

class Tarea_Evaluable(Tarea):
    id_tarea_evaluable = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profesores = models.ManyToManyField(Usuario)
    calificacion = models.FloatField()

    def __str__(self):
        return super().__str__() + f" - {self.profesores} - {self.calificacion}"