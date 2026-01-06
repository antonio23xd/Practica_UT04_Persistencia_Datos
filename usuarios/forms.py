from django import forms
from usuarios.models import Usuario

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