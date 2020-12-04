"""clairbuoyant_backend URL Configuration."""
from buoyant.views import BuoyView
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'buoys', BuoyView)

urlpatterns = [
    url('admin/', admin.site.urls),
]

urlpatterns += router.urls
