from django.db import models
from django.contrib.auth.models import User

class PitPrompt(models.Model):
	prompt = models.CharField(max_length=512)

	def __str__(self):
		return self.prompt
