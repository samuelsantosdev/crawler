from rest_framework import serializers
from api.serializers.feed_content_serializer import FeedContentSerializer

class FeedSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=256)
    link  = serializers.CharField(max_length=256)
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return FeedContentSerializer(obj['description'], many=True).data