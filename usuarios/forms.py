from django import forms
from usuarios.models import Tarea_Individual, Usuario

#Usuario Form
class UsuarioForm(forms.ModelForm):    
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'dni', 'email', 'rol')
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Introduce tu nombre', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    #Validaciones        
    def clean(self):
        cleaned_data = super().clean()        
        #Validación nombre
        if not cleaned_data.get('nombre'):
            self.add_error('nombre', 'El nombre no puede estar vacío.')
        #Validación apellidos
        if not cleaned_data.get('apellidos'):
            self.add_error('apellidos', 'Los apellidos no pueden estar vacíos.')            
        #Validación fecha_nacimiento
        if not cleaned_data.get('fecha_nacimiento'):
            self.add_error('fecha_nacimiento', 'La fecha de nacimiento no puede estar vacía.')
        #Validación DNI
        if not cleaned_data.get('dni'):
            self.add_error('dni', 'El DNI no puede estar vacío.')
        #Validación email
        if not cleaned_data.get('email'):
            self.add_error('email', 'El email no puede estar vacío.')
        #Validación rol
        if not cleaned_data.get('rol'):
            self.add_error('rol', 'El rol no puede estar vacío.')
        return cleaned_data

    #Guardar el Usuario
    def save(self, commit=True):
        if self.cleaned_data.get('rol') == 'ALUMNO':
            Alumno = super().save(commit=False)
            if commit:
                Alumno.save()
        else:
            Profesor = super().save(commit=False)
            if commit:
                Profesor.save()
        return super().save(commit)

#Tarea Individual Form
class TareaIndividualForm(forms.ModelForm):
    class Meta:
        model = Tarea_Individual
        fields = ('nombre_tarea', 'tipo_tarea', 'es_evaluable', 'fecha_entrega', 'alumno', 'profesores')
        widgets = {
            'nombre_tarea': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_tarea': forms.Select(attrs={'class': 'form-control'}),
            'es_evaluable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'profesores': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data.get('es_evaluable'))
        print(cleaned_data.get('profesores'))
        #Validación nombre_tarea
        if not cleaned_data.get('nombre_tarea'):
            self.add_error('nombre_tarea', 'El nombre de la tarea no puede estar vacío.')
        #Validación tipo_tarea
        if not cleaned_data.get('tipo_tarea'):
            self.add_error('tipo_tarea', 'El tipo de tarea no puede estar vacío.')
        #Validación profesores si es_evaluable es True
        if cleaned_data.get('es_evaluable') and not cleaned_data.get('profesores'):
            self.add_error('profesores', 'Debe seleccionar al menos un profesor para una tarea evaluable.')                 
        #Validación fecha_entrega
        if not cleaned_data.get('fecha_entrega'):
            self.add_error('fecha_entrega', 'La fecha de entrega no puede estar vacía.')
        #Validación alumno
        if not cleaned_data.get('alumno'):
            self.add_error('alumno', 'El alumno no puede estar vacío.')
        return cleaned_data
    
    def save(self, commit=True):
        tarea_individual = super().save(commit=False)
        if commit:
            tarea_individual.save()
        return super().save(commit)