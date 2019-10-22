from rest_framework import serializers

class FeedContentSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=256)
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return obj['content']

    