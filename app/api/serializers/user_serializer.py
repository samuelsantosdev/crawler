from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['url', 'username', 'password', 'email', 'is_staff']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username,
                            email=email)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj