from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Diss


@admin.register(Diss)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')




# Register your models here.
