from django import forms
from .models import LoginUsuario

class LoginUsuarioForm(forms.ModelForm):
	class Meta:
		model = LoginUsuario
		fields = ('usuario','password')

		widgets = {
			'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Usuario'}),
			'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Password'})
			}
