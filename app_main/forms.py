from django import forms
from .models import LoginUsuario

class LoginUsuarioForm(forms.ModelForm):
	class Meta:
		model = LoginUsuario
		fields = ('usuario','password')