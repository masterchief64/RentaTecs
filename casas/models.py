from django.db import models
from propietarios.models import Propietario

class Casa(models.Model):
	tipo_casa = models.CharField(max_length=20)
	renta = models.IntegerField(default=0)
	pago = models.CharField(max_length=20)
	direccion = models.CharField(max_length=255)
	cuartos = models.SmallIntegerField()
	banios = models.SmallIntegerField()
	pisos = models.SmallIntegerField()
	servicios = models.TextField()
	negocios_cercanos = models.TextField()
	tiempo_tec = models.TimeField()
	rutas_tec = models.CharField(max_length=255)
	casa_frente = models.ImageField(upload_to='casas/imagenes')
	casa_cuarto = models.ImageField(upload_to='casas/imagenes')
	casa_banio = models.ImageField(upload_to='casas/imagenes')
	casa_otra = models.ImageField(upload_to='casas/imagenes')
	propietario = models.ForeignKey(Propietario)

	def __unicode__(self):
		return self.direccion