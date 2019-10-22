from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from api.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer