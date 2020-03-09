from django.contrib.auth.models import User
from scouting.models import UserProfile, PitScouting, Competition, Team, PitPrompt
from rest_framework import viewsets
from django.core import serializers
from scouting.serializers import UserSerializer, UserProfileSerializer, PitScoutingSerializer, CompetitionSerializer, TeamSerializer, PitPromptSerializer


class PitScoutingViewSet(viewsets.ModelViewSet):
  queryset = PitScouting.objects.all()
  serializer_class = PitScoutingSerializer
  http_method_names = ['get', 'update', 'post', 'delete']