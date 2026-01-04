from django import forms
from usuarios.models import Alumno

class AlumnoForm(forms.ModelForm):    
    class Meta:
        model = Alumno
        fields = ("nombre", "apellidos", "fecha_nacimiento", "dni", "email")
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Introduce tu nombre', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
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
        if cleaned_data.get('fecha_nacimiento'):
            self.add_error('fecha_nacimiento', 'La fecha de nacimiento no puede estar vacía.')
        #Validación DNI
        if not cleaned_data.get('DNI'):
            self.add_error('DNI', 'El DNI no puede estar vacío.')
        #Validación email
        if not cleaned_data.get('email'):
            self.add_error('email', 'El email no puede estar vacío.')
        return cleaned_data

    #Guardar el Alumno
    def save(self, commit=True):
        Alumno = super().save(commit=False)
        if commit:
            Alumno.save()
        return super().save(commit)