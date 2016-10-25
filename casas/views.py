from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Casa


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

#@login_required
def ver_casas(request):
	casas = Casa.objects.all()
	return render(request, 'ver_casas.html', {'casas': casas})

def buscar(request, direccion):
	casas = Casa.objects.filter(direccion=direccion)
	return render(request, 'buscar.html', {'casas': casas})