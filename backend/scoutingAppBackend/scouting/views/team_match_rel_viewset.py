from scouting.models import TeamMatchRel, Match, Team, MatchData
from rest_framework import viewsets
from django.core import serializers
from scouting.serializers import TeamMatchRelSerializer, MatchSerializer, TeamSerializer, MatchDataSerializer


class TeamMatchRelViewSet(viewsets.ModelViewSet):
  queryset = TeamMatchRel.objects.all()
  serializer_class = TeamMatchRelSerializer
  http_method_names = ['get', 'update', 'post', 'delete']