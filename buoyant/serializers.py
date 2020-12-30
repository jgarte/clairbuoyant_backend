from buoyant.models import Buoy
from rest_framework import serializers


class BuoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buoy
        fields = [
            'id',
            'station_id',
            'name',
            'location',
            'owner',
            'pgm',
            'buoy_type',
            'met',
            'currents',
            'waterquality',
            'dart',
        ]
