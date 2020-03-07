from rest_framework import viewsets
from scouting.models import Competition
from django.core import serializers
from scouting.serializers import CompetitionSerializer


class CompetitionViewSet(viewsets.ModelViewSet):
  queryset = Competition.objects.all()
  serializer_class = CompetitionSerializer
  http_method_names = ['get', 'post', 'put', 'delete']