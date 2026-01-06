from django.urls import path
from usuarios.views import alta_usuario, visualizar_datos_alumno, visualizar_lista_alumnos

urlpatterns = [
    path('', visualizar_lista_alumnos, name='visualizar_lista_alumnos'),
    path('<uuid:id_alumno>/', visualizar_datos_alumno, name='visualizar_datos_alumno'),    
    path('alta_usuario', alta_usuario, name='alta_usuario'),
]