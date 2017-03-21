import uuid

from django.db import models


class ChannelManager(models.Manager):
    '''
    Channel's model Manager.
    '''
    def get_subcategories(self, channel, category):
        '''
        Get category subcategories, return an array of tuples.
        '''
        categories = []
        sub_categories = ChannelCategory.objects.filter(channel=channel,
                                                       parent_category=category)
        for sub_category in sub_categories:
            categories.append((sub_category.to_dict(),
                               self.get_subcategories(channel, sub_category)))

        return categories

    def get_categories_tree(self, channel):
        '''
        Get categories tree as an array of tuples.
        '''
        categories = []
        root_categories = ChannelCategory.objects.filter(channel=channel,
                                                         parent_category=None)
        for category in root_categories:
            categories.append((category.to_dict(),
                               self.get_subcategories(channel, category)))
        return categories 


class Channel(models.Model):
    '''
    Channel model.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    objects = ChannelManager()

    def __str__(self):
        return self.name


class ChannelCategoryManager(models.Manager):
    '''
    ChannelCategory model Manager.
    '''
    def get_near_categories(self, category):
        '''
        Get category parents and subcategories, and return them as an array of
        tuples.
        '''
        parents = []
        if category.parent_category != None:
            parents = self.get_parents(category.parent_category)
        children = self.get_subcategories(category)
        return parents, children

    def get_parents(self, category):
        '''
        Get category parents.
        '''
        cat = []
        if category.parent_category == None:
            return [category.to_dict()]
        else:
            cat.append(category.to_dict())
            cat += self.get_parents(category.parent_category)
            return cat

    def get_subcategories(self, category):
        '''
        Get category subcategories.
        '''
        categories = []
        sub_categories = ChannelCategory.objects.filter(parent_category=category)
        for sub_category in sub_categories:
            categories.append((sub_category.to_dict(), self.get_subcategories(sub_category)))
        return categories


class ChannelCategory(models.Model):
    '''
    ChannelCategory model.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel)
    parent_category = models.ForeignKey('self', null=True)
    objects = ChannelCategoryManager()

    def __str__(self):
        return self.name
    
    def to_dict(self):
        return {"id": str(self.id), "name": self.name}
