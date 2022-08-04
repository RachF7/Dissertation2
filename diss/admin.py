from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location
from diss.models import UserProfile


@admin.register(Location)
class SwimAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
    

admin.site.register(UserProfile)




