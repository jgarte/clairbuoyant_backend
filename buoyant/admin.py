from buoyant.models import Buoy, Observation
from django.contrib import admin


class BuoyantAdmin(admin.ModelAdmin): ...


admin.site.register(Buoy, BuoyantAdmin)
admin.site.register(Observation, BuoyantAdmin)
