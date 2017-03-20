from django.core.management.base import BaseCommand, CommandError

from channels.csv_importer import import_file

class Command(BaseCommand):
    help = 'Import channels category from csv.'

    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs='*')

    def handle(self, *args, **options):
        if len(options['arguments']) == 2:
            channel = options['arguments'][0]
            file = options['arguments'][1]
            import_file(channel, file)
            self.stdout.write(self.style.SUCCESS('Successfully imported categories'))
        else:
            self.stdout.write(self.style.ERROR('Usage: importcategories [category] [file]'))
