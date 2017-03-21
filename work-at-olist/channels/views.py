from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from channels.models import Channel, ChannelCategory
from channels.serializers import ChannelSerializer, CategorySerializer


# Create your views here.
class ChannelList(APIView):
    def get(self, request):
        '''
        List all channels.
        '''
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)


class CategoriesList(APIView):
    def get(self, request, uuid=None):
        '''
        List categories from a specific channel.
        '''
        try:
            channel = Channel.objects.get(id=uuid)
            channel_serializer = ChannelSerializer(channel)
        except Channel.DoesNotExist:
            raise Http404
        categories = Channel.objects.get_categories_tree(channel)
        return JsonResponse({'channel':channel_serializer.data, 
                             'categories': categories}, safe=False)


class Category(APIView):
    def get(self, request, uuid=None):
        '''
        List parent and children from a single category.
        '''
        try:
            category = ChannelCategory.objects.get(id=uuid)
            category_serializer = CategorySerializer(category)
        except ChannelCategory.DoesNotExist:
            raise Http404
        parent, children = ChannelCategory.objects.get_near_categories(category)
        return JsonResponse({'category': category_serializer.data,
                             'parent_categories': parent,
                             'sub_categories': children})
