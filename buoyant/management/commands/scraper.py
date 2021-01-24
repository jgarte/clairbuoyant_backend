from buoyant.services import NDBCScraper
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect buoy meterological data."

    def handle(self, *args, **kwargs):
        NDBCScraper()
        self.stdout.write("Task complete.")
