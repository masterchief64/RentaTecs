from django.db import models

class Alumno(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=60)
	apellido_paterno = models.CharField(max_length=60)
	foto = models.ImageField(upload_to='pictures/alumnos')
	no_control = models.CharField(max_length=8)
	nip = models.CharField(max_length=4)
	semestre = models.CharField(max_length=2)

	def __unicode__(self):
		return self.name