from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Collect buoy data."

    def handle(self, *args, **kwargs):
        self.stdout.write("This will trigger NDBC scraping.")
