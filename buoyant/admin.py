from buoyant.models import Buoy, Meteorological
from django.contrib import admin


class BuoyantAdmin(admin.ModelAdmin):
    ...


admin.site.register(Buoy, BuoyantAdmin)
admin.site.register(Meteorological, BuoyantAdmin)
