from django import forms
from productos.models import *
from django.forms import ModelForm

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ['username','first_name','last_name','password', 'email']
    def clean_password(self):
        if(len(self.cleaned_data['password'])<7):
            raise forms.ValidationError("Contraseña muy corta. Longitud mínima de 7 caracteres")
        return self.cleaned_data['password']
    def clean(self):
        cleaned_data=self.cleaned_data