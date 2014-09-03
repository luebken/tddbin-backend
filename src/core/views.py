from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import SessionSerializer
from .serializers import SpecSerializer
from django.contrib.auth.models import User
from .models import Spec
from .models import Session

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.filter(user_id=1)
    serializer_class = SessionSerializer

class UserSpecViewSet(viewsets.ModelViewSet):
    queryset = Spec.objects.filter(author_id=1)
    serializer_class = SpecSerializer

