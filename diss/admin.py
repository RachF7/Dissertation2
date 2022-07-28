from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location


@admin.register(Location)
class SwimAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')



