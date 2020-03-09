from django.db import models

class Competition(models.Model):
	name = models.CharField(max_length=512)
	date = models.DateField()
	location = models.CharField(max_length=1024)
	api = models.CharField(max_length=1024)

	def __str__(self):
		return f'{self.name}, {self.date}, {self.location}'



