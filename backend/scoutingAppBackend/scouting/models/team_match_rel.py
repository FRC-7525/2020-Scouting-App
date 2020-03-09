from django.db import models
from scouting.models import Match, Team, MatchData

class TeamMatchRel(models.Model):
	match = models.ForeignKey(Match, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	matchData = models.ForeignKey(MatchData, on_delete=models.CASCADE)