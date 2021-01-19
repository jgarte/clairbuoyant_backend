from buoyant.models import Buoy
from django.contrib import admin


class BuoyantAdmin(admin.ModelAdmin): ...


admin.site.register(Buoy, BuoyantAdmin)
