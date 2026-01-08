from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from usuarios.forms import TareaGrupalForm, TareaIndividualForm, UsuarioForm
from usuarios.models import Profesor, Tarea_Grupal, Tarea_Individual, Usuario, Alumno

# Create your views here.
#Dar alta usuario
def alta_usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario = usuario_form.save()
            if usuario.rol == 'ALUMNO':                
                alumno = Alumno(usuario=usuario)
                alumno.save()
            elif usuario.rol == 'PROFESOR':
                profesor = Profesor(usuario=usuario)
                profesor.save()            
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

#Crear tarea individual
def crear_tarea_individual(request):
    if request.method == 'POST':
        tarea_individual_form = TareaIndividualForm(request.POST)
        if tarea_individual_form.is_valid():
            tarea = tarea_individual_form.save()            
            messages.success(request, f'Tarea {tarea.nombre_tarea} creada correctamente.')
            return redirect('visualizar_lista_usuarios')
        else:
            print(tarea_individual_form.errors)
    else:
        tarea_individual_form = TareaIndividualForm()
    return render(request, 'creacion_tarea_individual.html', {'tarea_individual_form': tarea_individual_form})

#Crear tarea grupal
def crear_tarea_grupal(request):
    if request.method == 'POST':
        tarea_grupal_form = TareaGrupalForm(request.POST)
        if tarea_grupal_form.is_valid():
            tarea = tarea_grupal_form.save()            
            messages.success(request, f'Tarea {tarea.nombre_tarea} creada correctamente.')
            return redirect('visualizar_lista_usuarios')
        else:
            print(tarea_grupal_form.errors)
    else:
        tarea_grupal_form = TareaGrupalForm()
    return render(request, 'creacion_tarea_grupal.html', {'tarea_grupal_form': tarea_grupal_form})

#Visualizar las tareas del alumno
def visualizar_tareas_alumno(request, id_usuario):
    usuario = Usuario.objects.filter(id_usuario=id_usuario).first()    
    if usuario is None:
        raise Http404("Usuario no encontrado")
    alumno = Alumno.objects.filter(usuario=usuario).first()
    if alumno is None:
        raise Http404("Alumno no encontrado")
    tareas = Tarea_Individual.objects.filter(alumno=alumno.usuario)
    tareas_grupales = Tarea_Grupal.objects.filter(alumnos=alumno)
    if not tareas:
        messages.info(request, f'El alumno {usuario.nombre} {usuario.apellidos} no tiene tareas asignadas.')
    return render(request, 'visualizar_tareas_alumno.html', {'usuario': usuario, 'tareas': tareas, 'tareas_grupales': tareas_grupales})

#Visualizar las tareas del profesor
def visualizar_tareas_profesor(request, id_usuario):
    usuario = Usuario.objects.filter(id_usuario=id_usuario).first()    
    if usuario is None:
        raise Http404("Usuario no encontrado")
    profesor = Profesor.objects.filter(usuario=usuario).first()
    if profesor is None:
        raise Http404("Profesor no encontrado")
    tareas = Tarea_Individual.objects.filter(profesores=profesor.usuario)
    tareas_grupales = Tarea_Grupal.objects.filter(profesores=profesor)
    print(tareas)
    if not tareas:
        messages.info(request, f'El profesor {usuario.nombre} {usuario.apellidos} no tiene tareas asignadas.')
    return render(request, 'visualizar_tareas_profesor.html', {'usuario': usuario, 'tareas': tareas, 'tareas_grupales': tareas_grupales})