from django.conf.urls import include, url
from django.conf import settings

from . import views
from cuentas.models import LoginUsuario

urlpatterns = [
	url(r'^/', views.ingresar, name='ingresar'),
]







	
