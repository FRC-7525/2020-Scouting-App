from django.contrib.auth.models import User
from scouting.models import MatchData, UserProfile
from rest_framework import viewsets
from django.core import serializers
from scouting.serializers import MatchDataSerializer, UserSerializer, UserProfileSerializer


class MatchDataViewSet(viewsets.ModelViewSet):
  queryset = MatchData.objects.all()
  serializer_class = MatchDataSerializer
  http_method_names = ['get', 'update', 'post', 'delete']