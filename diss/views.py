
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.http import HttpResponse
def index(request):
    context_dict = {}
    return render(request, 'diss/index.html', context=context_dict)

def map(request):
    return render(request, 'diss/map.html', )

