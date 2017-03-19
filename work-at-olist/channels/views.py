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
        return render(request, template, {'channel':channel, 
                                          'categories': categories})

    def single(request):
        template = "single.html"
        category_id = request.GET.get('category_id', None)
        category = ChannelCategory.objects.get(id=category_id)
        categories = ChannelCategory.objects.get_near_categories(category)
        return render(request, template, {'category': category,
                                          'sub_categories': categories})
