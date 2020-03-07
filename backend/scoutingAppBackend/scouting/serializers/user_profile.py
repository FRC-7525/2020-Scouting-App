from django.contrib.auth.models import User
from scouting.models import UserProfile
from rest_framework import serializers

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('id', 'user',  'isAdmin', 'isGuest', 'name')