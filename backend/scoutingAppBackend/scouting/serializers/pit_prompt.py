from scouting.models import PitPrompt
from rest_framework import serializers

class PitPromptSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = PitPrompt
		fields = ('id', 'prompt')