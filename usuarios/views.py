from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages

from usuarios.forms import UsuarioForm
from usuarios.models import Alumno
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
        return redirect('visualizar_datos_alumno')
    else:
        usuario_form = UsuarioForm()
    return render(request, 'alta_usuario.html', {'usuario_form': usuario_form})

# Visualizar los datos personales de un alumno
def visualizar_datos_alumno(request, id_alumno):
    alumno = Alumno.objects.filter(id_alumno=id_alumno).first()
    if alumno is None:
        raise Http404("Alumno no encontrado")
    return render(request, 'visualizar_datos_alumno.html', {'alumno': alumno})

# Visualizar la lista de alumnos
def visualizar_lista_alumnos(request):
    #Recupero los usuarios de la base de datos
    lista_alumnos = Alumno.objects.all()
    print(lista_alumnos)
    return render(request, 'lista_alumnos.html', {'lista_alumnos': lista_alumnos})