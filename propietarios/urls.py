from django.conf.urls import include, url
from django.conf import settings

from . import views
from propietarios.models import Propietario

urlpatterns = [
	url(r'^ver_propietarios/', views.ver_propietarios, name='ver_propietarios'),
	url(r'^registrar/', views.registrar, name='registrar'),
	url(r'^mis_casas/(\d+)', views.mis_casas, name='mis_casas'),


]