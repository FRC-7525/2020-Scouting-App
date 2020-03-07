from django.db import models
from scouting.models import Competition, PitPrompt, Team, UserProfile

class PitScouting(models.Model):
	user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
	competition = models.ForeignKey(Competition, null=True, on_delete=models.SET_NULL)
	prompt = models.ForeignKey(PitPrompt, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	response = models.CharField(max_length=2048)

	def __str__(self):
		return f'Submitted by: {self.user}, for team: {self.team}'
