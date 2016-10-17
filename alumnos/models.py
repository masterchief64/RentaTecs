from django.db import models

class Alumno(models.Model):
	name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=60)
	picture = models.CharField(upload_to='pictures/alumns')
	no_control = models.CharField(max_length=8)
	nip = models.CharField(max_length=4)
	semester = models.CharField(max_length=2)