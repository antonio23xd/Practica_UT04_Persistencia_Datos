from django.urls import path
from usuarios.views import alta_usuario, crear_tarea_grupal, crear_tarea_individual, visualizar_datos_usuario, visualizar_lista_usuarios, visualizar_tareas_alumno, visualizar_tareas_profesor

urlpatterns = [
    path('', visualizar_lista_usuarios, name='visualizar_lista_usuarios'),
    path('<uuid:id_usuario>/', visualizar_datos_usuario, name='visualizar_datos_usuario'),    
    path('alta_usuario', alta_usuario, name='alta_usuario'),
    path('crear_tarea_individual', crear_tarea_individual, name='crear_tarea_individual'),
    path('crear_tarea_grupal', crear_tarea_grupal, name='crear_tarea_grupal'),
    path('tareas_alumno/<uuid:id_usuario>/', visualizar_tareas_alumno, name='visualizar_tareas_alumno'),
    path('tareas_profesor/<uuid:id_usuario>/', visualizar_tareas_profesor, name='visualizar_tareas_profesor'),
]