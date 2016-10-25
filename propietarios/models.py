from django.db import models

class Propietario(models.Model):
	nombre = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	telefono = models.CharField(max_length=14)
	celular = models.CharField(max_length=15)
	facebook = models.CharField(max_length=30)
	email = models.EmailField()
	whatsapp = models.CharField(max_length=15)

	def __unicode__(self):
		return self.nombre