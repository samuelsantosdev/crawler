from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from api.serializers.userserializer import UserSerializer

# ViewSets define the view behavior.
class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer