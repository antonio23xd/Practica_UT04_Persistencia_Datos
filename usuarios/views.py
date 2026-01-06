from django.shortcuts import redirect, render
from usuarios.forms import AlumnoForm
from django.contrib import messages
# Create your views here.
alumnos = [
        {"nombre": "Juan", "apellidos": "Pérez", "dni": "12345678A"},
        {"nombre": "María", "apellidos": "Gómez", "dni": "87654321B"},
    ]

#Dar alta alumno
def alta_alumno(request):
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST)
        if alumno_form.is_valid():
            alumno = alumno_form.save()
            messages.success(request, f'Alumno {alumno.nombre} {alumno.apellidos} creado correctamente.')
        else:
            print(alumno_form.errors)
        return redirect('visualizar_datos_alumno')
    else:
        alumno_form = AlumnoForm()
    return render(request, 'alta_alumno.html', {'alumno_form': alumno_form})

# Visualizar los datos personales de un usuario
def visualizar_datos_alumno(request):
    return render(request, 'DatosPersonales.html', {'datos': alumnos})


# Visualizar la lista de usuarios
def visualizar_lista_alumnos(request):
    return render(request, 'usuarios/lista_usuarios.html', {'alumnos': alumnos})
