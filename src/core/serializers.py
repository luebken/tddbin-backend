from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Session
from .models import Spec

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('name', 'user', 'started_at')

class SpecSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spec
        fields = ('code', 'session', 'author', 'tests_passed', 'saved_at')

