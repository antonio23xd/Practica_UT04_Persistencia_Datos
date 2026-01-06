from django.urls import path
from usuarios.views import alta_alumno, visualizar_datos_alumno, visualizar_lista_alumnos

urlpatterns = [
    path('', visualizar_lista_alumnos, name='visualizar_lista_alumnos'),
    path('<uuid:id_alumno>/', visualizar_datos_alumno, name='visualizar_datos_alumno'),    
    path('alta_alumno', alta_alumno, name='alta_alumno'),
]