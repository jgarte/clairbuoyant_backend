from buoyant.services import NDBCScraper_Buoy
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect buoy data."

    def handle(self, *args, **kwargs):
        NDBCScraper_Buoy()
        self.stdout.write("Task complete.")
