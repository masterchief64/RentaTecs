from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import LoginUsuario
from .forms import LoginUsuarioForm

def ingresar(request):
	if request.method == "POST":
		form = LoginUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = LoginUsuarioForm()
	return render(request, 'index.html', {'form': form})

