from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from api.serializers.userserializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer