from django.db import models

class LoginUsuario(models.Model):
	usuario = models.CharField(max_length=60)
	password = models.CharField(max_length=64)