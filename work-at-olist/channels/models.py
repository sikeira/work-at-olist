import uuid

from django.db import models


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ChannelCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    channel = models.ForeignKey(Channel)
    parent_category = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.name
