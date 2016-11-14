from django.shortcuts import render
from casas.models import Casa

def home(request):
	casas = Casa.objects.all()
	return render(request, 'index.html', {'casas':casas})