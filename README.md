# Práctica UT04 – Persistencia de Datos

## Descripción
Este proyecto gestiona usuarios con diferentes roles: **alumno** y **profesor**.

- El **alumno** puede crear tareas de distintos tipos:
  - Individual
  - Grupal
  - Evaluable o no evaluable
- El **profesor** puede evaluar o no las tareas creadas por los alumnos.

## Decisiones tomadas
### Relación Usuario – Alumno / Profesor
La tabla usuarios_usuario actúa como entidad principal para los usuarios del sistema. A partir de ella se definen los roles de alumno y profesor mediante tablas independientes (usuarios_alumno y usuarios_profesor), estableciendo una relación uno a uno (1:1).
### Relación Usuario – Tarea Individual
La tabla usuarios_tarea_individual mantiene una relación uno a muchos (1:N) con la tabla usuarios_usuario, mediante el campo alumno_id. Un usuario con rol de alumno puede crear múltiples tareas individuales, mientras que cada tarea individual pertenece a un único alumno.
### Relación Usuario – Tarea Grupal
La tabla usuarios_tarea_grupal se relaciona con usuarios_usuario mediante una relación uno a muchos (1:N). Un alumno puede crear varias tareas grupales, pero cada tarea grupal está asociada a un único alumno creador.
### Relación Tarea Individual – Tarea Evaluable Individual
Las tareas evaluables individuales se relacionan mediante la tabla usuarios_tarea_evaluable_individual, la cual mantiene una relación uno a uno (1:1) con usuarios_tarea_individual.
### Relación Tarea Grupal – Tarea Evaluable Grupal
Lla tabla usuarios_tarea_evaluable_grupal se relaciona en una relación uno a uno (1:1) con usuarios_tarea_grupal.
### Relación Profesor – Tareas Evaluables
La evaluación de las tareas se gestiona mediante relaciones muchos a muchos (N:M) entre los profesores y las tareas evaluables, tanto individuales como grupales.
Estas relaciones se implementan a través de tablas intermedias:
usuarios_tarea_evaluable_individual_profesor
usuarios_tarea_evaluable_grupal_profesor
Gracias a este diseño, un profesor puede evaluar múltiples tareas y una misma tarea puede ser evaluada por varios profesores.

**Relación**                                             **Tipo**
Usuario →           Alumno                                1 a 1
Usuario →           Profesor                              1 a 1
Usuario →           Tarea individual                      1 a N
Usuario →           Tarea grupal                          1 a N
Tarea individual →  Tarea evaluable individual            1 a 1
Tarea grupal →      Tarea evaluable grupal                1 a 1
Profesor ↔          Tarea evaluable individual            N a M
Profesor ↔          Tarea evaluable grupal                N a M

## Librerías necesarias para el proyecto
El proyecto incluye un archivo `requirements.txt` con todas las dependencias necesarias para su correcto funcionamiento.

### Instalación de dependencias
Ejecuta el siguiente comando para instalar las librerías:
```bash
pip install -r requirements.txt
```
## Datos iniciales
El proyecto incluye `fixtures`JSON para cargar los registros en la base de datos. Ejecutarlo después de las migraciones:
```bash
python3 manage.py loaddata datos_iniciales.json