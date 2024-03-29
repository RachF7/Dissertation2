from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location, forum, Discussion
from diss.models import UserProfile


@admin.register(Location)
class SwimAdmin(OSMGeoAdmin):
    list_display = ('name', 'address')
    

admin.site.register(UserProfile)

admin.site.register(forum)
admin.site.register(Discussion)




