from scouting.models import Match, Competition
from rest_framework import viewsets
from django.core import serializers
from scouting.serializers import MatchSerializer, CompetitionSerializer


class MatchViewSet(viewsets.ModelViewSet):
  queryset = Match.objects.all()
  serializer_class = MatchSerializer
  http_method_names = ['get', 'update', 'post', 'delete']