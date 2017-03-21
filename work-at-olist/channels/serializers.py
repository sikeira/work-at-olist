from rest_framework import serializers
from channels.models import Channel, ChannelCategory


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelCategory
        fields = ('id', 'name')
