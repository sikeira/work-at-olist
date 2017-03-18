import csv
from channels.models import Channel, ChannelCategory


def import_file(channel, file):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

