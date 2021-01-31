from buoyant.services import NDBCScraper_MetData
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect buoy meterological data."

    def handle(self, *args, **kwargs):
        NDBCScraper_MetData()
        self.stdout.write("Task complete.")
