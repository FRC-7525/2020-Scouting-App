from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
	name = models.CharField(max_length=512)
	number = models.CharField(max_length=64)

	def __str__(self):
		return f'{self.number}: {self.name}'
