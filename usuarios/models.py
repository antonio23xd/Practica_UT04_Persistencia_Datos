import uuid
from django.db import models

# Create your models here.
#Clase abstracta Usuario
class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.fecha_nacimiento} {self.dni} {self.email}"

#De momento dejamos las clases Profesor y Alumno vacías,
# solamente heredan de Usuario
class Profesor(Usuario):
    id_profesor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Alumno(Usuario):
    id_alumno = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)    

    def __str__(self):
        return super().__str__() + f" - {self.alumno}"

class Tarea_Grupal(Tarea):
    id_tarea_grupal = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__() + f" - {self.alumno}"

class Tarea_Evaluable(Tarea):
    id_tarea_evaluable = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profesores = models.ManyToManyField(Profesor)
    calificacion = models.FloatField()

    def __str__(self):
        return super().__str__() + f" - {self.profesores} - {self.calificacion}"