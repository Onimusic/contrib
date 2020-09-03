from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Temp'

    def handle(self, **other):
        call_command('collectstatic', interactive=False, clear=True)
