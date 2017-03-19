import uuid

from django.db import models


class ChannelManager(models.Manager):
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
    objects = ChannelManager()

    def __str__(self):
        return self.name


class ChannelCategoryManager(models.Manager):
    def get_near_categories(self, category):
        parents = self.get_parents(category)
        children = self.get_subcategories(category)
        if len(parents) > 0:
            categories = [(parents[0], children)]
            i = 1
            while i < len(parents):
                categories = [(parents[i], categories)]
                i += 1
            return categories
        else:
            return children

    def get_parents(self, category):
        cat = []
        if category.parent_category == None:
            return [category]
        else:
            cat.append(category)
            cat += self.get_parents(category.parent_category)
            return cat

    def get_subcategories(self, category):
        categories = []
        sub_categories = ChannelCategory.objects.filter(parent_category=category)
        for sub_category in sub_categories:
            categories.append((sub_category, self.get_subcategories(sub_category)))
        return categories


class ChannelCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel)
    parent_category = models.ForeignKey('self', null=True)
    objects = ChannelCategoryManager()

    def __str__(self):
        return self.name
