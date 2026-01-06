from django.urls import path
from usuarios.views import alta_usuario, visualizar_datos_usuario, visualizar_lista_usuarios

urlpatterns = [
    path('', visualizar_lista_usuarios, name='visualizar_lista_usuarios'),
    path('<uuid:id_usuario>/', visualizar_datos_usuario, name='visualizar_datos_usuario'),    
    path('alta_usuario', alta_usuario, name='alta_usuario'),
]