import csv
from channels.models import Channel, ChannelCategory


def import_file(channel_name, file):
    with open(file) as f:
        reader = csv.reader(f)
        try:
            channel = Channel.objects.get(name=channel_name) 
        except Channel.DoesNotExist:
            channel = Channel(name=channel_name)
            channel.save()
        for row in reader:
            if row[0] != 'Category':
                categories = row[0].split(' / ')
                i = 0
                category_objs = []
                while i < len(categories):
                    try:
                        if i == 0:
                            channel_category = ChannelCategory.objects.get(
                                                    name=categories[i],
                                                    channel=channel,
                                                    parent_category=None)
                        else:
                            channel_category = ChannelCategory.objects.get(
                                                    name=categories[i],
                                                    channel=channel,
                                                    parent_category=category_objs[i-1])

                    except ChannelCategory.DoesNotExist:
                        channel_category = ChannelCategory()
                        channel_category.name = categories[i]
                        channel_category.channel = channel
                    if i != 0:
                        channel_category.parent_category = category_objs[i-1]
                    channel_category.save()
                    category_objs.append(channel_category)
                    i += 1
