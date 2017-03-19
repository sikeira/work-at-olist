import uuid

from django.db import models


class ChannelCategoryManager(models.Manager):
    def get_subcategories(self, channel, category):
        categories = []
        sub_categories = ChannelCategory.objects.filter(channel=channel,
                                                       parent_category=category)
        for sub_category in sub_categories:
            categories.append((sub_category, self.get_subcategories(channel,
                                                                    sub_category)))

        return categories

    def get_categories_tree(self, channel):
        categories = []
        root_categories = ChannelCategory.objects.filter(channel=channel,
                                                         parent_category=None)
        for category in root_categories:
            categories.append((category, self.get_subcategories(channel,
                                                                category)))
        return categories 


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    objects = ChannelCategoryManager()

    def __str__(self):
        return self.name


class ChannelCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel)
    parent_category = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.name
