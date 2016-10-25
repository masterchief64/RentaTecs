from django.conf.urls import url
from . import views
from casas.models import Casa

urlpatterns = [
	url(r'^ver_casas/', views.ver_casas, name='ver_casas'),
	url(r'^buscar/(?P<direccion>[\w\-\W]+)/', views.buscar, name='buscar'),


]