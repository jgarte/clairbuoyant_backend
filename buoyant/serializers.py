from buoyant.models import Buoy, Meteorological
from rest_framework import serializers


class MeteorologicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meteorological
        fields = [
            "observation_date",
            "wind_speed",
            "wind_gust",
            "wave_height",
            "dom_wave_period",
            "avg_wave_period",
            "wave_dir",
            "sea_pressure",
            "air_temp",
            "sea_temp",
            "tide",
            "dewpoint_temp",
            "station_visibility",
            "pressure_tendency",
        ]


class BuoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buoy
        fields = [
            "id",
            "station_id",
            "name",
            "location",
            "owner",
            "pgm",
            "buoy_type",
            "met",
            "currents",
            "waterquality",
            "dart",
        ]
