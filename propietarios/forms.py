from django import forms
from .models import Propietario

class PropietarioForm(forms.ModelForm):
	class Meta:
		model = Propietario
		fields = ('nombre','apellidos','telefono','celular','facebook','email','whatsapp')

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Nombre'}),
			'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Nombre'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Telefono'}),
			'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Celular'}),
			'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Facebook'}),
			'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa Telefono'}),
			'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa WhatsApp'}),


			}
