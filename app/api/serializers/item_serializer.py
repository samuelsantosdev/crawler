from rest_framework import serializers
from api.serializers.feed_serializer import FeedSerializer

class ItemSerializer(serializers.Serializer):

    item = serializers.SerializerMethodField()

    def get_item(self, obj):
        return FeedSerializer(obj['item']).data