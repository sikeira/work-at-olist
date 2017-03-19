from django.conf.urls import url

from channels.views import ChannelsView


urlpatterns = [
    url(r'^channels/list', ChannelsView.list),
    url(r'^channels/categories', ChannelsView.categories),
    url(r'^channels/single', ChannelsView.single),
]
