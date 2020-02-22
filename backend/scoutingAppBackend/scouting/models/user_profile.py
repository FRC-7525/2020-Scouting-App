from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	isAdmin = models.BooleanField(default='False')
	isGuest = models.BooleanField(default='False')

	def __str__(self):
		return self.user.username



