from buoyant.models import Buoy
from buoyant.serializers import BuoySerializer
from rest_framework import viewsets


class BuoyView(viewsets.ModelViewSet):
    queryset = Buoy.objects.all()
    serializer_class = BuoySerializer
