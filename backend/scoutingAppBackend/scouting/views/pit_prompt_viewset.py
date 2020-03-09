from rest_framework import viewsets
from scouting.models import PitPrompt
from django.core import serializers
from scouting.serializers import PitPromptSerializer


class PitPromptViewSet(viewsets.ModelViewSet):
  queryset = PitPrompt.objects.all()
  serializer_class = PitPromptSerializer
  http_method_names = ['get', 'post', 'put', 'delete']