from scouting.models import PitScouting, Competition, PitPrompt, Team, UserProfile
from rest_framework import serializers

class PitScoutingSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PitScouting
		fields = ('id', 'user', 'competition', 'prompt', 'team', 'response')