from django.urls import path
from usuarios.views import visualizar_datos_alumno

urlpatterns = [
    path('', visualizar_datos_alumno, name='visualizar_datos_alumno'),   
]