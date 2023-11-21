from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def base_layout(request):
    template = 'habitat_pwa/base.html'
    return render(request, template)
