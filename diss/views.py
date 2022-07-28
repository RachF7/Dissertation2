
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.http import HttpResponse
import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Location


def index(request):
    context_dict = {}
    return render(request, 'diss/index.html', context=context_dict)


def map(request):
    return render(request, 'diss/map.html', )


class MarkersMapView(TemplateView):

    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["location"] = json.loads(serialize("geojson", Location.objects.all()))
        return context

