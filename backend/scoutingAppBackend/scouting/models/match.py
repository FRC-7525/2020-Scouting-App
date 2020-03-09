from django.db import models
from scouting.models import Competition

class Match(models.Model):
	competition = models.ForeignKey(Competition, null=True, on_delete=models.SET_NULL)
	difference = models.IntegerField(default=0)

