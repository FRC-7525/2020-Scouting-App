from django.contrib.auth.models import User
from scouting.models import UserProfile
from rest_framework import viewsets
from django.core import serializers
from scouting.serializers import UserSerializer, UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileSerializer
  http_method_names = ['get', 'update', 'post', 'delete']