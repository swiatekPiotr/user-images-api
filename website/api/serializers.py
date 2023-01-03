from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Picture

import os
import base64


class PictureSerializer(serializers.ModelSerializer):
    photo_binary = serializers.SerializerMethodField('get_photo_binary')
    photo = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail_200', 'thumbnail__200x200'),
            ('thumbnail_400', 'thumbnail__400x400'),
        ]
    )

    class Meta:
        model = Picture
        fields = ['id', 'title', 'date', 'photo', 'photo_binary']

    def get_photo_binary(self, obj):
        with open((os.getcwd()+obj.photo.url), 'rb') as img_file:
            img_data = base64.b64encode(img_file.read()).decode('utf-8')
        return img_data

    def create(self, validated_data):
        return Picture.objects.create(**validated_data)
