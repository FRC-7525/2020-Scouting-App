from django.db import models
from django.contrib.auth.models import User
from scouting.models import UserProfile

class MatchData(models.Model):
	user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
	controlPanel = models.BooleanField(default='False')
	highPort = models.BooleanField(default='False')
	lowPort = models.BooleanField(default='False')
	hang = models.BooleanField(default='False')
	autonomousPoints = models.IntegerField(default=0)
	teleopPoints = models.IntegerField(default=0)
	isBlueTeam = models.BooleanField(default='False')
	autoHighPort = models.BooleanField(default='False')
	autoLowPort = models.BooleanField(default='False')
	malfunction = models.BooleanField(default='False')
	blockedShots = models.IntegerField(default=0)
	trench = models.BooleanField(default='False')
	positionalControlPanel = models.BooleanField(default='False')
	balancedHang = models.BooleanField(default='False')
	highPortShots = models.IntegerField(default=0)
	lowPortShots = models.IntegerField(default=0)
	hazardousWiring = models.BooleanField(default='False')
	isLongshot = models.BooleanField(default='False')
	isSweeper = models.BooleanField(default='False')
	isDefender = models.BooleanField(default='False')




