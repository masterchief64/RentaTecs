from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Propietario
from casas.models import Casa
from .forms import PropietarioForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def ver_propietarios(request):
	propietarios = Propietario.objects.all()
	return render(request, 'ver_propietarios.html', {'propietarios': propietarios} )

def registrar(request):
	if request.method == "POST":
		form = PropietarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/propietarios/mis_casas/')
	else:
		form = PropietarioForm()
	return render(request, 'registrar.html', {'form':form})

def ingresar(request):
	if request.method = 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid():
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()

	return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

def mis_casas(request, id_propietario):
	pass