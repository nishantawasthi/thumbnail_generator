from rest_framework import serializers

from rest_api.models import Thumbnail


class ThumbnailSerializer(serializers.ModelSerializer):
    """
    Serializer for Thumbnail model.
    """
    class Meta:
        model = Thumbnail
        fields = ['name', 'image']
