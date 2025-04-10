from django import forms
from django.contrib.auth.models import User
from .models import Prenda

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password

class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = ['nombre', 'talle', 'precio']
