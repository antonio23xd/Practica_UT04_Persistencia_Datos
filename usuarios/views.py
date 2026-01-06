from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages

from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
# Create your views here.
alumnos = [
        {"nombre": "Juan", "apellidos": "Pérez", "dni": "12345678A"},
        {"nombre": "María", "apellidos": "Gómez", "dni": "87654321B"},
    ]

#Dar alta alumno
def alta_usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario = usuario_form.save()
            messages.success(request, f'Usuario {usuario.nombre} {usuario.apellidos} creado correctamente.')
        else:
            print(usuario_form.errors)
        return redirect('visualizar_lista_usuarios')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'alta_usuario.html', {'usuario_form': usuario_form})

# Visualizar los datos personales de un usuario
def visualizar_datos_usuario(request, id_usuario):
    usuario = Usuario.objects.filter(id_usuario=id_usuario).first()
    if usuario is None:
        raise Http404("Usuario no encontrado")
    return render(request, 'visualizar_datos_usuario.html', {'usuario': usuario})

# Visualizar la lista de usuarios
def visualizar_lista_usuarios(request):
    #Recupero los usuarios de la base de datos
    lista_usuarios = Usuario.objects.all()
    print(lista_usuarios)
    return render(request, 'lista_usuarios.html', {'lista_usuarios': lista_usuarios})