from scouting.models import Match, Competition
from rest_framework import serializers

class MatchSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Match
		fields = ('id', 'competition', 'difference')