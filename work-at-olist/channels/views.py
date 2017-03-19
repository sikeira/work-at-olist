from django.shortcuts import render

from channels.models import Channel, ChannelCategory

# Create your views here.
class ChannelsView:
    def list(request):
        template = 'home.html'
        channels = Channel.objects.all()
        return render(request, template, {'channels': channels})


    def categories(request):
        template = 'categories.html'
        channel_id = request.GET.get('channel_id', None)
        channel = Channel.objects.get(id=channel_id)
        categories = Channel.objects.get_categories_tree(channel)
        return render(request, template, {'categories': categories})
