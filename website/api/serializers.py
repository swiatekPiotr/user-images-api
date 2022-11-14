from rest_framework import serializers
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Picture
        fields = ['title', 'photo']

    def get_photo_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.photo.url)
