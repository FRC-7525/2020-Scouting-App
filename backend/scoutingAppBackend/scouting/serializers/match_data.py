from scouting.models import MatchData, UserProfile
from rest_framework import serializers

class MatchDataSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MatchData
		fields = ('id', 'user', 'controlPanel', 'highPort', 'lowPort', 'hang', 'autonomousPoints', 'teleopPoints', 'isBlueTeam', 'autoHighPort', 'autoLowPort',	'malfunction', 'blockedShots', 'trench', 'positionalControlPanel', 'balancedHang', 'highPortShots', 'lowPortShots', 'hazardousWiring', 'isLongshot', 'isSweeper', 'isDefender')
