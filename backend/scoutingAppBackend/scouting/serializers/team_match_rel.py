from scouting.models import TeamMatchRel, Match, Team, MatchData
from scouting.serializers import MatchSerializer, TeamSerializer, MatchDataSerializer
from rest_framework import serializers

class TeamMatchRelSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = TeamMatchRel
		fields = ('id', 'match', 'team', 'matchData')