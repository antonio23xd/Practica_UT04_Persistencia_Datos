from django.urls import path
from usuarios.views import alta_alumno, visualizar_datos_alumno

urlpatterns = [
    path('', visualizar_datos_alumno, name='visualizar_datos_alumno'),
    path('alta_alumno', alta_alumno, name='alta_alumno'),
]