from buoyant.models import Buoy, Meteorological
from buoyant.serializers import BuoySerializer, MeteorologicalSerializer
from rest_framework import viewsets


class BuoyView(viewsets.ModelViewSet):
    queryset = Buoy.objects.all()
    serializer_class = BuoySerializer


class MetView(viewsets.ModelViewSet):
    queryset = Meteorological.objects.all()
    serializer_class = MeteorologicalSerializer
