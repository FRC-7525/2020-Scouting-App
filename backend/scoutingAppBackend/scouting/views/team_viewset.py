from rest_framework import viewsets
from scouting.models import Team
from django.core import serializers
from scouting.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
  queryset = Team.objects.all()
  serializer_class = TeamSerializer
  http_method_names = ['get', 'post', 'put', 'delete']