from scouting.models import Competition
from rest_framework import serializers

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Competition
		fields = ('id', 'name', 'date', 'location', 'api')